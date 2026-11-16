from langgraph.graph import StateGraph, START, END
from typing import TypedDict
class State(TypedDict):
    question : str
    status :str
    category: str

def process_question(state: State):
    return {
        "status":"processed"
    }

def analyze_question(state: State):
    return {
        "category":"technical"
    }

def route_question(state: State):
    if state["category"] == "technical":
        return "technical_agent"
    return "general_agent"

graph = (
    StateGraph(State)
    .add_node("process_question",process_question)
    .add_edge(START,"process_question")
    .add_node("analyze_question",analyze_question)
    .add_edge("process_question", "analyze_question")
    .add_edge("analyze_question", END)
    
    .compile()
)

graph.invoke({"question": "what is an LLM?","status":"pending"})