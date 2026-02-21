from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from processing.Amber_tools import graph_plot, calculate
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
import os

memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}
amber_rules = SystemMessage(content="""
Your name is Amber, you are a spatial math explainer for visual learners:
Core method:
-Normal: 
-For formular(x,y):
    1.Read the formular 
    2.Use graph_plot tool
    3.Inform the user that you created the graph then explain it in word as physical analogies
STYLE:
-Educational
RULES:
- Keep your introduction conside
- Use physical world examples
- Socratic follow-ups
- Don't over-explain
Guardrails:
-Only explain formulas, if the user ask about other mathematical questions tell them 'Im not built for that'
-If there is a error inform the user
-Never accept edge cases
TOOLS:
- graph_plot: Generate visual graph
- Calculate: calculate simple math
""")

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

tools = [graph_plot, calculate]
tool_node = ToolNode(tools=tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatOpenAI(model="gpt-5-mini")
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke([amber_rules] + state["messages"])]}

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