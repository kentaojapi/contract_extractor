import logging
import os
import sys

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings

load_dotenv()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def initialize_vectorstore():
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


def load_from_pdf(file_path: str) -> list:
    loader = PyPDFLoader(file_path)
    raw_docs = loader.load()
    logger.info("Loaded %d documents", len(raw_docs))
    print(raw_docs)

    def clean_text(text):
        return text.replace(' ', '').replace('\n', '').replace('\u3000', '')

    cleaned_documents = []
    for doc in raw_docs:
        cleaned_text = clean_text(doc.page_content)
        doc.page_content = cleaned_text
        cleaned_documents.append(doc)
    print(cleaned_documents)

    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    docs = text_splitter.split_documents(raw_docs)
    logger.info("Split %d documents", len(docs))
    return docs


if __name__ == "__main__":
    file_path = sys.argv[1]
    vectorstore = initialize_vectorstore()
    docs = load_from_pdf(file_path)
    vectorstore.add_documents(docs)
