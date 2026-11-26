from backend.app.agents.context_builder import build_context
result = build_context(retrieval_result=" ")

assert "Chunk ID:" in result
assert "Source:" in result
assert "Content:" in result