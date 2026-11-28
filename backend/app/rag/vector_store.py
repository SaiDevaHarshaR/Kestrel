
import json
import math
import sqlite3
from pathlib import Path

from google import genai
from ..core.config import settings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DB_PATH = PROJECT_ROOT / "kestrel_vectors.db"
KNOWLEDGE_PATH = PROJECT_ROOT / "knowledge" / "kestrel_knowledge.md"

# Gemini client
embedding_client = genai.Client(
    api_key=settings.gemini_api_key.get_secret_value()
)

EMBEDDING_MODEL = "gemini-embedding-001"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            document TEXT NOT NULL,
            metadata TEXT NOT NULL,
            embedding TEXT NOT NULL
        )
    """)
    return conn


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    response = embedding_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=texts
    )

    if not response.embeddings:
        raise RuntimeError("Gemini returned no embeddings.")

    return [item.values for item in response.embeddings]


def add_document(text: str, source: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    if not chunks:
        return

    embeddings = generate_embeddings(chunks)

    if len(chunks) != len(embeddings):
        raise RuntimeError("Embedding count does not match chunk count.")

    with get_connection() as conn:
        for i, chunk in enumerate(chunks):
            document_id = f"{source}_{i}"

            metadata = {
                "source": source,
                "chunk_index": i
            }

            conn.execute("""
                INSERT OR REPLACE INTO documents
                (id, document, metadata, embedding)
                VALUES (?, ?, ?, ?)
            """, (
                document_id,
                chunk,
                json.dumps(metadata),
                json.dumps(embeddings[i])
            ))


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot_product = sum(x * y for x, y in zip(a, b))

    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def retrieve_documents(question: str, n_results: int = 3):
    query_embedding = generate_embeddings([question])[0]

    with get_connection() as conn:
        rows = conn.execute("""
            SELECT id, document, metadata, embedding
            FROM documents
        """).fetchall()

    ranked_results = []

    for document_id, document, metadata, embedding in rows:
        stored_embedding = json.loads(embedding)

        similarity = cosine_similarity(
            query_embedding,
            stored_embedding
        )

        ranked_results.append({
            "id": document_id,
            "document": document,
            "metadata": json.loads(metadata),
            "distance": 1 - similarity
        })

    ranked_results.sort(
        key=lambda item: item["distance"]
    )

    selected = ranked_results[:n_results]

    return {
        "documents": [item["document"] for item in selected],
        "ids": [item["id"] for item in selected],
        "metadatas": [item["metadata"] for item in selected],
        "distances": [item["distance"] for item in selected]
    }


def ingest_knowledge_base():
    with open(KNOWLEDGE_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    add_document(
        content,
        source="kestrel_knowledge.md"
    )


class VectorStore:
    """Small compatibility interface for existing count checks."""

    def count(self) -> int:
        with get_connection() as conn:
            return conn.execute(
                "SELECT COUNT(*) FROM documents"
            ).fetchone()[0]


collection = VectorStore()
