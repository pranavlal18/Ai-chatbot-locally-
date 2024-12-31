# AI Chatbot with Streamlit and Ollama

This project is a simple AI chatbot built using **Streamlit** for the user interface and **Ollama** for the language model. The chatbot allows users to ask questions and displays the conversation history with a logo embedded in the title and responses.

## Features

- **Interactive Chat Interface**: Users can type questions and get responses from the AI model.
- **Conversation History**: Displays the full conversation history with user inputs and bot responses.
- **Streaming Responses**: The bot's responses are streamed in real-time for a better user experience.

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **Streamlit**: Install using `pip install streamlit`
3. **Ollama**: Install the Ollama library using `pip install langchain-ollama`
4. **Logo Image**: Place your logo image (e.g., `llama.png`) in the `logo` folder within the project directory.

## Setup

### Step 1: Clone the Repository
Clone the repository to your local machine:
bash
git clone https://github.com/your-username/your-repo.git
cd your-repo


### Step 2: Install Dependencies
Install the required Python libraries:

bash
Copy
pip install -r requirements.txt
### Step 3: Install Ollama
Ollama is required to run the language model locally. Follow these steps to install it:

macOS/Linux:
Run the following command in your terminal:

bash
Copy
curl -fsSL https://ollama.ai/install.sh | sh
Windows (using WSL):
Install Windows Subsystem for Linux (WSL) if you haven’t already:

bash
Copy
wsl --install
Install Ollama in WSL:

bash
Copy
curl -fsSL https://ollama.ai/install.sh | sh
### Step 4: Download a Model
Ollama supports various models, such as Llama, Mistral, and others. To download a model, use the ollama pull command.

Download the llama2 model:

bash
Copy
ollama pull llama2
Verify the downloaded models:

bash
Copy
ollama list
### Step 5: Add Logo
Place your logo image (e.g., llama.png) in the logo folder within the project directory. Ensure the logo path in the code matches the actual file location.

### Step 6: Run the Application
Start the Streamlit app:

bash
Copy
streamlit run app.py
### Step 7: Access the Chatbot
Open your browser and navigate to http://localhost:8501.
