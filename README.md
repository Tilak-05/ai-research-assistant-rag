# AI Research Assistant (RAG + NLP)

AI Research Assistant is a Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask natural language questions about their content. The system processes the document, generates embeddings, stores them in a vector database, and retrieves relevant information to generate accurate answers with citations.

This project demonstrates how modern AI systems such as document search assistants, research copilots, and knowledge retrieval systems are built using LLMs and vector databases.

---

# Features

Document Upload
Users can upload PDF documents directly through the web interface.

Semantic Search
The system converts document text into vector embeddings and performs similarity search to find the most relevant content.

Question Answering
Users can ask questions in natural language and receive AI-generated answers based on the document.

Source Citations
Answers include references to the original document pages.

Interactive Chat Interface
A chat-style interface allows users to interact with the document similar to modern AI assistants.

Error Handling
The system detects PDFs that do not contain readable text and informs the user.

---

# System Architecture

The system follows a Retrieval-Augmented Generation (RAG) pipeline.

Document Upload
User uploads a PDF document.

Document Processing
The PDF text is extracted and split into smaller chunks.

Embedding Generation
Each chunk is converted into numerical vector embeddings.

Vector Storage
Embeddings are stored in a FAISS vector database.

Retriever
The retriever finds the most relevant chunks based on the user query.

Language Model
The LLM generates an answer using the retrieved document context.

Response Generation
The system returns the answer along with document citations.

---

# Project Structure

```
ai-research-assistant-rag
│
├── backend
│   ├── ingestion
│   │   ├── pdf_loader.py
│   │   ├── text_splitter.py
│   │   └── embeddings.py
│   │
│   ├── retrieval
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── generation
│   │   ├── llm.py
│   │   └── rag_chain.py
│   │
│   └── utils
│
├── frontend
│   └── streamlit_app.py
│
├── scripts
│   ├── build_vector_db.py
│   └── query_documents.py
│
├── data
│   └── raw_pdfs
│
├── vector_store
│   └── faiss_index
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

Programming Language
Python

Libraries and Frameworks
LangChain
HuggingFace Transformers
FAISS
Streamlit

Machine Learning Models
Sentence Transformers (all-MiniLM-L6-v2) for embeddings
FLAN-T5 for language generation

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-research-assistant-rag.git
cd ai-research-assistant-rag
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit application

```
streamlit run frontend/streamlit_app.py
```

Open in browser

```
http://localhost:8501
```

Upload a PDF and begin asking questions about the document.

---

# Example Workflow

1. Upload a research paper or PDF document
2. The system extracts and processes the text
3. Document chunks are converted into embeddings
4. Embeddings are stored in the FAISS vector database
5. User asks a question
6. The retriever finds the most relevant document sections
7. The LLM generates an answer using those sections

---

# Limitations

Handwritten notes or scanned documents may not work because they contain images instead of machine-readable text.

Future versions may include OCR support to process scanned documents.

---

# Future Improvements

Multi-document knowledge base

Conversation memory for follow-up questions

OCR support for scanned documents

PDF preview inside the application

Advanced retrieval with reranking models

Deployment on cloud platforms

---

# Use Cases

Research paper analysis

Document question answering

Internal knowledge base assistants

Technical documentation search

Academic study assistants

---

