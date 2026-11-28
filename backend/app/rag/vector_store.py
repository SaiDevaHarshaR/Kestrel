
import os
import chromadb

from google import genai
from ..core.config import settings
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ["GEMINI_API_KEY"] = settings.gemini_api_key.get_secret_value()

# Gemini client
embedding_client = genai.Client(
    api_key=settings.gemini_api_key.get_secret_value()
)

# Fresh ChromaDB collection, without a built-in embedding function
client = chromadb.PersistentClient(path="./chroma_manual")

collection = client.get_or_create_collection(
    name="kestrel_knowledge"
)


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    response = embedding_client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts
    )

    return [item.values for item in response.embeddings]


def add_document(text: str, source: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    texts = splitter.split_text(text)

    if not texts:
        return

    ids = [f"{source}_{i}" for i in range(len(texts))]

    metadatas = [
        {"source": source, "chunk_index": i}
        for i in range(len(texts))
    ]

    embeddings = generate_embeddings(texts)

    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings
    )


def retrieve_documents(question: str):
    query_embedding = generate_embeddings([question])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return {
        "documents": results["documents"][0],
        "ids": results["ids"][0],
        "metadatas": results["metadatas"][0],
        "distances": results["distances"][0]
    }


def ingest_knowledge_base():
    with open(
        "knowledge/kestrel_knowledge.md",
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    add_document(content, source="kestrel_knowledge.md")
