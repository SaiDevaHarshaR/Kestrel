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
    ids = [str(uuid.uuid4()) for chunk in chunks]
    metadatas = [
    {"source": source}
    for chunk in chunks]

    collection.add(
        ids=ids,
        documents=text,
        metadatas=metadatas
    )
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0
    )

    texts = text_splitter.split_text(text)
