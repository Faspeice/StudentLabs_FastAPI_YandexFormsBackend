from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_prefix: str = "/api"
    db_url: str = f"postgresql+asyncpg://postgres:23685585@localhost/postgres"
    db_echo: bool = False


settings = Settings()
