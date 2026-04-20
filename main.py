import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.globals import set_debug
set_debug(True)

st.title("Ask Anything")

with st.sidebar:
    st.title("LLM Settings")
    model_name = st.selectbox("Select model", ["qwen3:1.7b", "qwen3:8b"])
if not model_name:
    st.info("Please select a model from the sidebar.")
    st.stop()

llm=ChatOllama(model=model_name)

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
