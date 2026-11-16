from langgraph.graph import StateGraph, START, END
from typing import TypedDict
class State(TypedDict):
    question : str

def process_question(state: State):
    return state
graph = (
    StateGraph(State)
    .add_node("process_question",process_question)
    .add_node(START,process_question)
    .add_node("process_question",END)
    .complie()
)

graph.invoke({"text": "what is an LLM?"})