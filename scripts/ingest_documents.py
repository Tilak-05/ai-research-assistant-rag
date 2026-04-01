import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.ingestion.pdf_loader import load_pdf
from backend.ingestion.text_splitter import split_documents


def main():

    file_path = "data/raw_pdfs/Baggage AI report.pdf"

    # Load PDF
    documents = load_pdf(file_path)

    print(f"Pages loaded: {len(documents)}")

    # Split into chunks
    chunks = split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    # Show first chunk
    print("\nFirst chunk preview:\n")
    print(chunks[0].page_content[:500])


if __name__ == "__main__":
    main()