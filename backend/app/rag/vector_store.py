import chromadb
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction
from ..core.config import settings
import uuid
client =  chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="my_collection",
    embedding_function=GoogleGeminiEmbeddingFunction(
        api_key = settings.gemini_api_key.get_secret_value(),
        model_name="gemini-embedding-001"
    )
)
collection.add(
    ids=,
    documents=________,
    metadatas=________
)
def add_document(text: str, source: str):
    ids = [str(uuid.uuid4()) for chunk in chunks]
    metadatas = [
    {"source": source}
    for chunk in chunks]
