import chromadb
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction
from ..core.config import settings
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter
client =  chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="my_collection",
    embedding_function=GoogleGeminiEmbeddingFunction(
        api_key = settings.gemini_api_key.get_secret_value(),
        model_name="gemini-embedding-001"
    )
)

def add_document(text: str, source: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    texts = text_splitter.split_text(text)
    ids = [str(uuid.uuid4()) for chunk in texts]
    metadatas = [
    {"source": source}
    for chunk in texts]

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )

def retrieve_documents(question: str):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    return results["documents"]