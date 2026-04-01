
import sys
import os
sys.path.append(os.getcwd())

import streamlit as st
from langchain_community.vectorstores import FAISS

from backend.ingestion.pdf_loader import load_pdf
from backend.ingestion.text_splitter import split_documents
from backend.ingestion.embeddings import load_embeddings
from backend.retrieval.vector_store import create_vector_store
from backend.retrieval.retriever import get_retriever
from backend.generation.llm import load_llm
from backend.generation.rag_chain import build_rag_chain


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Assistant")
st.caption("Ask questions from your uploaded research papers")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("Upload Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type="pdf"
    )

    st.markdown("---")
    st.markdown("Built with RAG + LangChain")

# Process uploaded PDF
if uploaded_file:

    save_path = os.path.join("data/raw_pdfs", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing document..."):

        documents = load_pdf(save_path)

        chunks = split_documents(documents)

        if len(chunks) == 0:
            st.error("No readable text found in this PDF.")
            st.stop()

        embeddings = load_embeddings()

        vector_db = create_vector_store(chunks, embeddings)

        retriever = get_retriever(vector_db)

        llm = load_llm()

        qa_chain = build_rag_chain(llm, retriever)

        st.session_state.qa_chain = qa_chain

    st.success("Document ready for questions!")

# Chat Interface
if "qa_chain" in st.session_state:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a question about the document")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = st.session_state.qa_chain.invoke(
                    {"query": prompt}
                )

                answer = response["result"]

                st.markdown(answer)

                with st.expander("Sources"):

                    for doc in response["source_documents"]:
                        st.write(
                            f"Page: {doc.metadata.get('page')}"
                        )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )