from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from ..llm.client import client
from ..llm.service import generate_response
from google.genai import errors
import time
from .context_builder import build_budgeted_context


class State(TypedDict):
    question: str
    status: str
    category: str
    context: str
    prompt: str

def retrieve_context(state: State ):
    question = state["question"]
    context = build_budgeted_context(question, 10000)
    return {"context" : context}

def process_question(state: State):
    return {"status": "processed"}

def analyze_question(state: State):
    question = state["question"]

    prompt = f"""
    Classify the following question into exactly one category:
    - technical
    - general

    Return only the category. No explanation.

    Question: {question}
    """
    last_error = None

    for attempt in range(3):
        try:
            response = client.models.generate_content( model="gemini-3.8-flash", contents=prompt)

            if not response or not response.text:
                raise ValueError("Gemini returned an empty response")
            result = response.text.strip().lower()
            if result in ["technical", "general"]:
                return {"category": result}
            last_error = ValueError(f"Invalid category returned: {result}")
        except errors.APIError as e:
            last_error = e
        if attempt < 2:
            time.sleep(2 ** attempt)
    raise RuntimeError( "Question classification failed after 3 attempts") from last_error

def technical_agent(state: State):
    prompt = f"""
    You are Kestrel's technical assistant.
    Use ONLY the supplied context.
    If the answer isn't present in the context, explicitly say you don't have enough information.

    Context:
    {state["context"]}

    Question:
    {state["question"]}
    """

    answer = generate_response(prompt)
    return {"status": "technical_reviewed", "answer": answer}

def general_agent(state: State):
    prompt = f"""
    You are Kestrel's general assistant.
    Use ONLY the supplied context.
    If the answer isn't present in the context, explicitly say you don't have enough information.

    Context:
    {state["context"]}

    Question:
    {state["question"]}
    """
    answer = generate_response(prompt)
    return {"status": "general_reviewed", "answer":answer}
def route_question(state: State) -> Literal["technical_agent", "general_agent"]:
    if state["category"] == "technical":
        return "technical_agent"
    return "general_agent"
graph = (
    StateGraph(State)
    .add_node("retrieve_context",retrieve_context)
    .add_node("process_question", process_question)
    .add_node("analyze_question", analyze_question)
    .add_node("technical_agent", technical_agent)
    .add_node("general_agent", general_agent)
    .add_edge(START, "retrieve_context")
    .add_edge("retrieve_context", "process_question")
    .add_edge("process_question", "analyze_question")
    .add_conditional_edges(
        "analyze_question",
        route_question,
        {  "technical_agent": "technical_agent",
            "general_agent": "general_agent"})
    .add_edge("technical_agent", END)
    .add_edge("general_agent", END)
    .compile()
)


result = graph.invoke({
    "question": "What is an LLM?",
    "status": "pending",
    "category": "",
    "context": ""
})

print(result)
