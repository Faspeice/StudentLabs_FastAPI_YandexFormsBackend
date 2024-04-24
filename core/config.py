from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DbSettings(BaseModel):
    url: str = f"postgresql+asyncpg://postgres:23685585@localhost/postgres"
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db: DbSettings = DbSettings()


settings = Settings()
