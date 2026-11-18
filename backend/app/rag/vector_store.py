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
def add_document(text: str, source: str):

