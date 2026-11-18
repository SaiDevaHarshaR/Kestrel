from .vector_store import retrieve_documents
from ..llm.client import client
def joining(question: str):
    chunks = retrieve_documents(question)
    context = " ".join(chunks[0])
    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
    )
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    return response.text