import streamlit as st
import streamlit.components.v1 as components
from processing.Amber_graph import final_state

st.title("Amber: The Function Partner")

if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_text := st.chat_input("User: "):
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
    total_input = 0
    total_output = 0
    total = 0
    with st.chat_message("assistant"):
        final = final_state(user_text)
        respond = final['messages'][-1]
        metadata = respond.response_metadata

        if "token_usage" in metadata:
            usage = metadata["token_usage"]
            itoken = usage["prompt_tokens"]
            utoken = usage["completion_tokens"]
        total_input += itoken
        total_output += utoken
        total += itoken + utoken

        if user_text.lower() in ["exit", "quit"]:
            st.markdown(f"[Token usage] in: {total_input} out: {total_output} total: {total}")
        else:
            message = respond.content
            st.markdown(message)
            if "created the graph" in message.lower():
                with open("graph.html", "r", encoding="utf8") as f:
                    html_data = f.read()
                components.html(html_data, height=600, scrolling=True)
    if not user_text.lower() in ["exit", "quit"]:
        st.session_state.messages.append({"role": "assistant", "content": message})