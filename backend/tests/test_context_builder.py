from backend.app.agents.context_builder import build_context
retrieval_result = {
    "documents": ["Chunk A", "Chunk B", "Chunk C"],
    "ids": ["chunk_0", "chunk_1"],
    "metadatas": [
        {"source": "knowledge.md"},
        {"source": "knowledge.md"},
        {"source": "knowledge.md"}
    ]
}
result = build_context(retrieval_result)

assert "FastAPI" in result
assert "Chunk ID:" in result
assert "Source:" in result
assert "Content:" in result

result1 = build_context({})
assert result1 == "No retrieval results"





