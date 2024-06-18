import langchain
from dotenv import load_dotenv
from fastapi import FastAPI
from routers import contracts

load_dotenv()
langchain.debug = True


app = FastAPI()
app.include_router(contracts.router)
