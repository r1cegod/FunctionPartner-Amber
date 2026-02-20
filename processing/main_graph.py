from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from processing.tools import calculate
from dotenv import load_dotenv
import os

memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

tools = [calculate]
tool_node = ToolNode(tools=tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]
llm = ChatOpenAI(model="gpt-5-mini")
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
bot_graph = graph_builder.compile(checkpointer=memory)

def final_state(user_text):
    return bot_graph.invoke({
        "messages":[
            {"role": "user", "content": user_text}
        ]},
        config=config
    )