from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from ..llm.client import client

class State(TypedDict):
    question : str
    status :str
    category: str

def process_question(state: State):
    return {
        "status":"processed"
    }

def analyze_question(state: State):
    question = state["question"]
    if "LLM" in question:
        return {"category": "technical"}
    else:
        return {"category": "general"}


    
def technical_agent(state: State):
    return {"status" : "technical_reviewed"}
def general_agent(state:State):
    return {"status":"general_reviewed"}
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
    .add_node("technical_agent", technical_agent)
    .add_node("general_agent", general_agent)
    .add_conditional_edges("analyze_question",route_question,{"technical_agent": "technical_agent","general_agent": "general_agent"})
    .add_edge("general_agent", END)
    .add_edge("technical_agent", END)
    .compile()
)

graph.invoke({"question": "what is an LLM?","status":"pending"})