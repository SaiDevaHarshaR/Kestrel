import chromadb
import os
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction

client =  chromadb.PersistentClient(path="./chroma_db")
collection = client.create_collection(
    name="my_collection",
    embedding_function=GoogleGeminiEmbeddingFunction(
        api_key=os.getenv("GEMINI_API_KEY"),
        model_name="gemini-embedding-001"
    )
)