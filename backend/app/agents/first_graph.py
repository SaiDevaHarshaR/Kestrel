from langgraph.graph import StateGraph, START, END
from typing import TypedDict
class State(TypedDict):
    question : str
    status :str
    technical:str

def process_question(state: State):
    return {
        "status":"processed"
    }


graph = (
    StateGraph(State)
    .add_node("process_question",process_question)
    .add_edge(START,"process_question")
    .add_node("analyze_question",)
    .add_edge("process_question",END)
    .compile()
)

graph.invoke({"question": "what is an LLM?","status":"pending"})