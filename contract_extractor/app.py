from collections.abc import Callable

import langchain
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from routers import contracts

load_dotenv()
langchain.debug = True


app = FastAPI()
app.include_router(contracts.router)


@app.middleware("http")
async def add_my_headers(request: Request, call_next: Callable) -> Response:
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
