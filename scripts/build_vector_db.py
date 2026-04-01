import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.ingestion.pdf_loader import load_pdf
from backend.ingestion.text_splitter import split_documents
from backend.ingestion.embeddings import load_embeddings
from backend.retrieval.vector_store import create_vector_store


def main():

    file_path = "data/raw_pdfs/Baggage AI report.pdf"

    # Load PDF
    documents = load_pdf(file_path)

    # Split into chunks
    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    # Load embeddings
    embeddings = load_embeddings()

    # Create vector database
    vector_db = create_vector_store(chunks, embeddings)

    # Save database
    vector_db.save_local("vector_store/faiss_index")

    print("Vector database created successfully")


if __name__ == "__main__":
    main()