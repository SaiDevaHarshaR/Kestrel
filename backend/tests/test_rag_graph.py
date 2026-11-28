
from backend.app.agents.first_graph import graph

def test_technical_question():
    result = graph.invoke({
        "question": "What framework does Kestrel use for its backend?"
    })

    print("\n--- Technical Test ---")
    print("Status:", result.get("status"))
    print("Answer:", result.get("answer"))
    print("Context:", result.get("context"))

    assert result.get("status") == "technical_reviewed"
    assert result.get("answer")
    assert "FastAPI" in result["answer"]


def test_general_question():
    result = graph.invoke({
        "question": "What are the main goals of Kestrel?"
    })

    print("\n--- General Test ---")
    print("Status:", result.get("status"))
    print("Answer:", result.get("answer"))

    assert result.get("status") == "general_reviewed"
    assert result.get("answer")


if __name__ == "__main__":
    test_technical_question()
    test_general_question()
    print("\nAll RAG graph tests passed!")
