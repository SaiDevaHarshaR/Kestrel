from ..llm.client import client
def count_tokens(text: str) -> int:
    total_tokens = client.models.count_tokens(model="gemini-3.8-flash", contents=text)
    return total_tokens.total_tokens
def calculate_input_budget(reserved_output_tokens: int, context_window: int) -> int:
    if context_window < reserved_output_tokens:
        raise ValueError("Reserved output tokens are more than context window")
    remaining_input = context_window-reserved_output_tokens
    return remaining_input

def is_within_budget(text: str, input_budget: int) -> bool:
    return count_tokens(text) <= input_budget

def select_chunks(retrieval_result: dict, input_budget: int):
    documents = retrieval_result.get("documents") or []
    selected_chunks = []
    for document in enumerate(documents):
        pass
    return "\n\n".join(selected_chunks)