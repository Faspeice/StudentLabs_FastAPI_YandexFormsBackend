from contextlib import asynccontextmanager

from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated
from items_views import router as items_router
from users.views import router as users_router
import uvicorn
from api import router as router_api1
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_api1, prefix=settings.api_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
