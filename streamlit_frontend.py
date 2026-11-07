import streamlit as st
import uuid

from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

st.title("QWENGPT")

# Initialize session state
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

# Thread configuratio
CONFIG = {
    "configurable":{
        "thread_id" : st.session_state["thread_id"]
    }
}

# Display previous conversation
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
    



user_input = st.chat_input("Type your message:")

if user_input:
    st.session_state["message_history"].append({
        "role":"user",
        "content":user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = chatbot.invoke({"messages":[HumanMessage(content = user_input)]},config = CONFIG)

            assistant_response = response["messages"][-1].content

            st.write(assistant_response)


    st.session_state["message_history"].append({
        "role":"assistant",
        "content":assistant_response
    })
