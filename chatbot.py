from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question:
Question: {question}
Answer: 
"""

model=OllamaLLM(model="llama3.2")
prompt=ChatPromptTemplate.from_template(template)
chain = prompt | model



def handle_conversation():
    print("Ask me anything | enter exit")
    while True:
        user=input("You: ")
        if user.lower() == "exit":
            break
        result=chain.invoke({"question":user})
        print("Bot: ",result)


if __name__=="__main__":
    handle_conversation()