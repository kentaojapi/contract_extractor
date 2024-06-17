import langchain
from add_document import initialize_vectorstore
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from structure.data_in_contract import DataInContract

load_dotenv()
langchain.debug = True


class ChatModel:
    DEFAULT_MODEL = "gpt-4o"

    def __init__(self, model_name: str = DEFAULT_MODEL, temperature: int = 0) -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.model = self._initialize_model()

    def _initialize_model(self) -> ChatOpenAI:
        return ChatOpenAI(
            model_name=self.model_name, temperature=self.temperature
        ).bind(response_format={"type": "json_object"})

    def get(self) -> ChatOpenAI:
        return self.model


class Template:
    TEMPLATE_FILE: str = "./prompts/extract_template.md"

    def __init__(self) -> None:
        pass

    def get(self) -> PromptTemplate:
        template = self._load_markdown()
        return PromptTemplate.from_template(template)

    def _load_markdown(self) -> str:
        with open(self.TEMPLATE_FILE, encoding="utf-8") as file:  # noqa: PTH123
            return file.read()


def get_details(file_name: str) -> dict:
    prompt = Template().get()
    retriever = initialize_vectorstore().as_retriever(
        search_kwargs={"k": 4, "filter": {"source": file_name}}
    )

    model = ChatModel().get()
    chain = (
        {"context": retriever}
        | prompt
        | model
        | JsonOutputParser(pydantic_object=DataInContract)
    )

    return chain.invoke("")
