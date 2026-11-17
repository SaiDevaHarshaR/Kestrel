from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from ..llm.client import client
from google.genai import errors

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
    last_api_error = None
    invalid_response = False
    prompt = f"Classify this following question as technical or general : {question}"

    for attempt in range(3):
        try:
            response = client.models.generate_content(model="gemini-3.8-flash",contents=prompt)
            res = response.text.strip().lower()
            if res in ["technical", "general"]:
                return {"category": res}
            else:
                invalid_response = True
        except errors.APIError as e:
            last_api_error = e
    if last_api_error is not None:
        raise HTTPException(status_code=502, detail="Gemini API failed after 3 attempts") from last_api_error
    raise ValueError("Gemini returned an invalid category")



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