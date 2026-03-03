from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from processing.Amber_graph import get_graph
from langchain_core.messages import ToolMessage

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

bot_graph = get_graph()

class ChatRequest(BaseModel):
    message: str

#NOT GET :)
@app.post("/user_chat")
def final_state(request: ChatRequest):
    config = {"configurable": {"thread_id": "1"}}
    result = bot_graph.invoke({
        "messages":[
            {"role": "user", "content": request.message},
        ]},
        config=config)
    graph_data = None
    for msg in result["messages"]:
        if isinstance(msg, ToolMessage) and str(msg.content).startswith("GRAPH:"):
            parts = msg.content.split(":")
            graph_data = {
                "type": parts[1],
                "coefficients": [float(x) for x in parts[2].split(",")]
            }
    return {
        "messages": result["messages"],
        "graph": graph_data
    }