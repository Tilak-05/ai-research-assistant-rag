from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embeddings):
    """
    Create FAISS vector database from document chunks
    """

    db = FAISS.from_documents(chunks, embeddings)

    return db