from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


def load_llm():
    """
    Load a local LLM for answering questions
    """

    pipe = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_length=512,
        temperature=0.1
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm