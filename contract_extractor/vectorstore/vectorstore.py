import os
from functools import lru_cache

from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings


@lru_cache
def initialize_vectorstore() -> Pinecone:
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)
