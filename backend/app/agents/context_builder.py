
def build_context(retrieval_result: dict) -> str:
    documents = retrieval_result.get("documents") or []
    ids = retrieval_result.get("ids") or []
    metadata = retrieval_result.get("metadatas") or []

    chunks = []

    for i, document in enumerate(documents):
        chunks.append(
            f"Chunk ID: {ids[i]}\n"
            f"Source: {metadata[i].get('source', 'Unknown')}\n"
            f"Content: {document}"
        )

    return "\n\n".join(chunks) if chunks else "No retrieval results"

def build_budgeted_context(question:str , input_budget: int)->str: 
    pass