import logging
import os
import sys
from functools import lru_cache

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Pinecone
from langchain_core.documents.base import Document
from langchain_openai import OpenAIEmbeddings

load_dotenv()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


@lru_cache
def initialize_vectorstore() -> Pinecone:
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


class PDFLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @staticmethod
    def _clean_text(text: str) -> str:
        return (
            text.replace(" ", "")
            .replace("\n", "")
            .replace("\u3000", "")
            .replace("\u2003", "")
        )

    def _clean_and_update_doc(self, doc: Document) -> Document:
        cleaned_text = self._clean_text(doc.page_content)
        doc.page_content = cleaned_text
        return doc

    def run(self) -> list[Document]:
        loader = PyPDFLoader(self.file_path)
        raw_docs = loader.load()
        logger.info("Loaded %d documents", len(raw_docs))
        print(raw_docs)

        cleaned_documents = list(map(self._clean_and_update_doc, raw_docs))
        print(cleaned_documents)

        text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
        docs = text_splitter.split_documents(raw_docs)
        logger.info("Split %d documents", len(docs))
        return docs


if __name__ == "__main__":
    file_path = sys.argv[1]
    vectorstore = initialize_vectorstore()
    docs = PDFLoader(file_path).run()
    vectorstore.add_documents(docs)
