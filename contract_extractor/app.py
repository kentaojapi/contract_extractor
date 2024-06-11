import langchain
from add_document import initialize_vectorstore
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv()
langchain.debug = True


class ChatModel:
    DEFAULT_MODEL = "gpt-3.5-turbo"

    def __init__(
            self, model_name: str = DEFAULT_MODEL, temperature: int = 0) -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.model = self._initialize_model()

    def _initialize_model(self) -> ChatOpenAI:
        return ChatOpenAI(model_name=self.model_name, temperature=self.temperature)

    def get(self) -> ChatOpenAI:
        return self.model


class Template:
    TEMPLATE = """以下の文脈だけを踏まえて質問に回答してください。
また、回答においてはcontextに含まれる文字列のみを単語で返答してください。

{context}

Question: {question}
"""

    def __init__(self) -> None:
        pass

    def get(self) -> PromptTemplate:
        return PromptTemplate.from_template(self.TEMPLATE)


def main() -> None:
    prompt = Template().get()
    retriever = initialize_vectorstore().as_retriever()

    model = ChatModel().get()
    chain = (  # noqa: F841
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    result = chain.invoke(input("例: 契約者甲の会社名は？"))
    print(result)


if __name__ == "__main__":
    main()
