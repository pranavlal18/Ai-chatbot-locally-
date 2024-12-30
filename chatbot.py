import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question:
Question: {question}
Answer: 
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

st.title("AI Chatbot")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

user_input = st.text_input("Ask me anything:", st.session_state.user_input)

if st.button("Get Response"):
    if user_input.lower() == "exit":
        st.write("Exiting...")
    else:
        result = chain.invoke({"question": user_input})
        st.session_state.conversation_history.append(f"You: {user_input}")
        st.session_state.conversation_history.append(f"Bot: {result}")
        for message in st.session_state.conversation_history:
            st.write(message)
        st.session_state.user_input = ""