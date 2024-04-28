from contextlib import asynccontextmanager

from fastapi import FastAPI, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated
from users.views import router as users_router
import uvicorn
from api import routerForm, routerAns
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=routerForm, prefix=settings.api_prefix)
app.include_router(router=routerAns, prefix=settings.api_prefix)
app.include_router(users_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
