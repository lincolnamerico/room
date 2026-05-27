from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://room:room@localhost:5432/room"
    debug: bool = False

    model_config = {"env_file": ".env"}


settings = Settings()
