from pydantic_settings import BaseSettings
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class DbSettings(BaseModel):
    url: str = (
        f"postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@"
        f"{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"
    )
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db: DbSettings = DbSettings()


settings = Settings()
