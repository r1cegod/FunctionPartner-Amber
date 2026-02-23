import streamlit as st
import streamlit.components.v1 as components
from processing.Amber_graph import final_state

st.set_page_config(layout="wide", page_title="Function partner Amber v0.2")
col1, col2 = st.columns([0.6, 0.4])

if "latest_graph_html" not in st.session_state:
    st.session_state.latest_graph_html = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_input" not in st.session_state:
    st.session_state.total_input = 0
if "total_output" not in st.session_state:
    st.session_state.total_output = 0
if "total" not in st.session_state:
    st.session_state.total = 0

with col2:
    st.header("Chat")
    chat_container = st.container(height=600)
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    if user_text := st.chat_input("User: "):
        st.session_state.messages.append({"role": "user", "content": user_text})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_text)
            if user_text.lower() in ["exit", "quit"]:
                st.markdown(f"[Token usage] in: {st.session_state.total_input} out: {st.session_state.total_output} total: {st.session_state.total}")
            else:
                with st.chat_message("assistant"):
                    final = final_state(user_text)
                    respond = final['messages'][-1]
                    metadata = respond.response_metadata
                if "token_usage" in metadata:
                    usage = metadata["token_usage"]
                    itoken = usage["prompt_tokens"]
                    utoken = usage["completion_tokens"]
                st.session_state.total_input += itoken
                st.session_state.total_output += utoken
                st.session_state.total += itoken + utoken
                message = respond.content
                st.markdown(message)
                if "created the graph" in message.lower():
                    with open("graph.html", "r", encoding="utf8") as f:
                        st.session_state.latest_graph_html = f.read()
                if not user_text.lower() in ["exit", "quit"]:
                    st.session_state.messages.append({"role": "assistant", "content": message})

with col1:
    st.header("Workspace")
    if st.session_state.latest_graph_html:
        components.html(st.session_state.latest_graph_html, height=600, scrolling=True)
    else:
        st.info("No graph yet💔")