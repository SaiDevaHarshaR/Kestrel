from ..llm.client import client

def count_tokens(text: str) -> int:
    total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=text
)
    return total_tokens.total_tokens
