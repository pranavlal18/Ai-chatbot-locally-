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


st.title("Chatbot")


user_input = st.text_input("Ask me anything:", "")


if st.button("Get Response"):
    if user_input.lower() == "exit":
        st.write("Exiting...")
    else:
        
        result = chain.invoke({"question": user_input})
        
        
        st.write(f"**You**: {user_input}")
        st.write(f"**Bot**: {result}")
