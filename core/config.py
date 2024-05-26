from pydantic_settings import BaseSettings
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class DbSettings(BaseModel):
    url: str = "postgresql+asyncpg://postgres:postgres@db:5432/foo"
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db: DbSettings = DbSettings()


settings = Settings()
