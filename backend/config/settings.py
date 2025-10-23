"""Settings module for the app."""

import os
from dotenv import load_dotenv
from functools import lru_cache
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """Settings class for the security chatbot app."""

    HOST: str = "localhost"
    PORT: int = 8000
    LOG_LEVEL: str = "DEBUG"
    LOG_FILE: Optional[str] = None

    DEBUG: bool = False

    DATABASE_URL: str = "sqlite:///./stories.db"
    API_PREFIX: str = "/api"
    ALLOWED_ORIGINS: str = ""

    GROQ_API_KEY: str
    DEFAULT_MODEL: str = "llama-3.1-8b-instant"
    DEFAULT_TEMPERATURE: float = 0.0

    def __init__(self, **values):
        super().__init__(**values)

        if self.DATABASE_URL == "sqlite:///./stories.db" and not self.DEBUG:
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT", "5432")
            db_name = os.getenv("DB_NAME")

            if all([db_user, db_password, db_host, db_name]):
                self.DATABASE_URL = (
                    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
                )

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        if not v or v == "*":
            return ["*"]
        return v.split(",") if v else ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings():
    """Get the settings for the app."""

    environment = os.getenv("ENVIRONMENT", "local")
    if environment == "local":
        return Settings(_env_file=".env", _env_file_encoding="utf-8", DEBUG=True)
    elif environment == "production":
        return Settings(HOST="0.0.0.0", DEBUG=False)
    else:
        raise ValueError(
            f"Invalid environment, expected 'local' or 'production' but got '{environment}'"
        )


if __name__ == "__main__":
    settings = get_settings()
    print(f"Host: {settings.HOST}")
    print(f"Port: {settings.PORT}")
    print(f"Database: {settings.DATABASE_URL}")