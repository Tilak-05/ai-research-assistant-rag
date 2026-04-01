def get_retriever(vector_db):
    """
    Create retriever for semantic search
    """

    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    return retriever