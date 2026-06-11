import streamlit as st

from run_graph import ask_question

st.set_page_config(
    page_title="IPL Intelligence Assistant",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 IPL Intelligence Assistant")
st.markdown(
    "Multi-Agent RAG using LangGraph + ChromaDB + Groq"
)

question = st.text_input(
    "Ask an IPL Question"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = ask_question(question)

        st.success("Answer")

        st.write(answer)