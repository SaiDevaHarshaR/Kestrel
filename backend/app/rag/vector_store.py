import chromadb
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction
from ..core.config import settings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="kestrel_knowledge",
    embedding_function=GoogleGeminiEmbeddingFunction(
    model_name="gemini-embedding-001",
    api_key_env_var="GEMINI_API_KEY"
))
def add_document(text: str, source: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    texts = splitter.split_text(text)
    ids = [
        f"{source}_{i}"
        for i, chunk in enumerate(texts)
    ]
    metadatas = [
        {"source": source, "chunk_index": i}
        for i, chunk in enumerate(texts)
    ]
    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )
def retrieve_documents(question: str):
    results = collection.query(
        query_texts=[question],
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