import os
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA


llm = ChatGroq(temperature=0.1, groq_api_key="Your Groq API Key", model_name="llama-3.3-70b-versatile") # Faster Loading since we use API
# llm = ChatOllama(model='llama3') # Completley on local

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 PDF Chatter")

# Function to process the PDF and create the vector index (cached for efficiency)
@st.cache_data(show_spinner=False)
def process_pdf(file_path):
    loaders = [UnstructuredPDFLoader(file_path)]
    index = VectorstoreIndexCreator(
        embedding=OllamaEmbeddings(model="llama3"),
        text_splitter=CharacterTextSplitter(chunk_size=1700, chunk_overlap=0)
    ).from_loaders(loaders)
    return index

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    binary_data = uploaded_file.getvalue()
    
    col1, col2 = st.columns([3, 1]) 
    
    with col1:
        pdf_viewer(input=binary_data, width=700)

    # Save the uploaded PDF
    pdf_folder_path = "./temp_files/"
    os.makedirs(pdf_folder_path, exist_ok=True)
    pdf_path = os.path.join(pdf_folder_path, uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with col2:
        with st.spinner("Processing PDF... Please wait."):
            index = process_pdf(pdf_path)

        st.sidebar.header("Chat with Your PDF")
        question = st.sidebar.text_input("Ask a question:")
        if question:
            with st.spinner("Searching for answers..."):
                chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=index.vectorstore.as_retriever(),
                    input_key="question"
                )
                answer = chain.run(question)
            st.sidebar.write("### Answer:")
            st.sidebar.write(answer)

else:
    st.info("Please upload a PDF file to begin.")
    st.sidebar.info("Upload a PDF to enable the chat feature.")
