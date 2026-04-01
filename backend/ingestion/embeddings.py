from langchain_community.embeddings import HuggingFaceEmbeddings


def load_embeddings():
    """
    Load embedding model for converting text into vectors
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings