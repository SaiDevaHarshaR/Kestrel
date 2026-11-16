from langgraph.graph import StateGraph, START, END
from typing import TypedDict
class State(TypedDict):
    question : str

def process_question(state: State):
    return state