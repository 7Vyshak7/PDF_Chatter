# PDF_Chatter
Welcome to PDF Chatter, a user-friendly and efficient tool that allows you to interact with PDF documents using natural language queries. Built with Streamlit and LangChain, this application uses state-of-the-art open-source language models like Llama to provide instant and accurate responses to your questions based on the content of uploaded PDFs. The intuitive interface and fast processing make it easy for anyone to extract insights from their documents effortlessly.
## Features
- Interactive PDF Viewer: View uploaded PDFs directly in the app.
- Natural Language Querying: Ask questions about the content of your PDF and get answers instantly.
- Efficient PDF Processing: Uses advanced embeddings and vector databases for quick document indexing and retrieval.
- Streamlined User Experience: Upload a PDF, type your question, and get answers with just a few clicks.
- Open-Source Models: Powered by Llama models, ensuring cost-effective and privacy-focused operation.
## Installation Guide
Follow these steps to set up and run PDF Chatter on your local system:

### Step 1: Install Required Libraries

Ensure you have Python installed (version 3.9 or higher). Then, install the necessary libraries:

```bash
pip install streamlit langchain streamlit-pdf-viewer langchain_ollama langchain_groq langchain_community
```

### Step 2: Install and Configure Ollama
To use Ollama embeddings or models, download and install the Ollama app:
- Visit the [Ollama Website](https://ollama.com/) to download the app.
- Follow the installation instructions for your operating system.
- Once installed, ensure the Ollama service is running.

### Step 3: Set Up Groq API (Optional)
If you prefer faster processing using Groq, sign up for a Groq API key:
- Visit the [Groq Website](https://groq.com/).
- Obtain your API key.
- Replace "Your Groq API Key" in the code with your actual key.

## Running the Demo
Clone this repository or download the code files:
```
git clone https://github.com/your-username/PDF_Chatter.git
cd PDF_Chatter
```
Start the Streamlit app:
```
streamlit run PdfChatApp.py
```
Open your browser and navigate to the URL provided by Streamlit (e.g., http://localhost:8501).
Upload a PDF file and start chatting with it!

## Acknowledgments
This project leverages the power of:
- LangChain
- Streamlit
- Ollama
- Groq

## Demo 🎥


https://github.com/user-attachments/assets/dc737609-937f-4539-ace4-0ffac5d5864e



