import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_community.vectorstores import FAISS
from backend.ingestion.embeddings import load_embeddings
from backend.retrieval.retriever import get_retriever
from backend.generation.llm import load_llm
from backend.generation.rag_chain import build_rag_chain


def main():

    # Load embeddings
    embeddings = load_embeddings()

    # Load vector database
    vector_db = FAISS.load_local(
        "vector_store/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Create retriever
    retriever = get_retriever(vector_db)

    # Load LLM
    llm = load_llm()

    # Build RAG pipeline
    qa_chain = build_rag_chain(llm, retriever)

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        response = qa_chain.invoke({"query": question})

        print("\nAnswer:\n", response["result"])

        print("\nSources:")
        for doc in response["source_documents"]:
            print("Page:", doc.metadata.get("page", "unknown"))



if __name__ == "__main__":
    main()