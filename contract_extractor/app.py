from fastapi import FastAPI
from routers import contracts

app = FastAPI()
app.include_router(contracts)
