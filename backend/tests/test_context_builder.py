from backend.app.agents.context_builder import build_context
retrieval_result = {
    "documents": ["FastAPI is Kestrel's backend framework."],
    "ids": ["chunk_0"],
    "metadatas": [{"source": "kestrel_knowledge.md"}]
}
result = build_context(retrieval_result)

assert "FastAPI" in result
assert "Chunk ID:" in result
assert "Source:" in result
assert "Content:" in result

result1 = build_context({})

assert result1 == "No retrieval results"

