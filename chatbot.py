import streamlit as st
import os
import base64  # Import the base64 module
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question:
Question: {question}
Answer: 
"""

model = OllamaLLM(model="llama3.2", streaming=True)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

project_dir = os.getcwd()
logo_path = os.path.join(project_dir, "logo", "llama.png")

if not os.path.exists(logo_path):
    st.error(f"Logo not found at: {logo_path}")
else:
    # Embed the logo in the title using HTML and CSS
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; font-size: 2.5em; font-weight: bold;">
            AI ChatB<img src="data:image/png;base64,{encoded_logo}" width="40" style="margin: 0px;">T
        </div>
        """,
        unsafe_allow_html=True
    )

    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    user_input = st.text_input("Ask me anything:", st.session_state.user_input)

    if st.button("Get Response"):
        if user_input.lower() == "exit":
            st.write("Exiting...")
        else:
            st.session_state.conversation_history.append(f"You: {user_input}")
            response_placeholder = st.empty()
            full_response = ""
            for chunk in chain.stream({"question": user_input}):
                full_response += chunk
                response_placeholder.markdown(f"Bot: {full_response}")
            st.session_state.conversation_history.append((logo_path, full_response))
            st.session_state.user_input = ""

    st.markdown("### Conversation History :")
    for message in st.session_state.conversation_history:
        if isinstance(message, tuple):
            logo, response = message
            col1, col2 = st.columns([1, 20])
            with col1:
                st.image(logo, width=40)
            with col2:
                st.markdown(f"<div style='margin-left: -10px;'>:&nbsp&nbsp&nbsp;{response}</div>", unsafe_allow_html=True)
        else:
            st.write(message)