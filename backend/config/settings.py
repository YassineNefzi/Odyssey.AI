"""Settings module for the app."""

import os
from dotenv import load_dotenv
from functools import lru_cache
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    """Settings class for the security chatbot app."""

    # Server settings
    HOST: str = "localhost"
    PORT: int = 8000
    LOG_LEVEL: str = "DEBUG"
    LOG_FILE: Optional[str] = None

    DATABASE_URL: str
    API_PREFIX: str
    ALLOWED_ORIGINS: str = ""

    # LLM settings
    GROQ_API_KEY: str
    DEFAULT_MODEL: str = "meta-llama/llama-4-maverick-17b-128e-instruct"
    DEFAULT_TEMPERATURE: float = 0.0

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings():
    """Get the settings for the app."""

    environment = os.getenv("ENVIRONMENT", "local")
    if environment == "local":
        return Settings(_env_file=".env", _env_file_encoding="utf-8")
    elif environment == "production":
        return Settings(HOST="0.0.0.0")
    else:
        raise ValueError(
            f"Invalid environment, expected 'local' or 'production' but got '{environment}'"
        )


# Example usage (for testing purposes)
if __name__ == "__main__":
    settings = get_settings()
    print(f"Host: {settings.HOST}")
    print(f"Port: {settings.PORT}")
    print(f"Log Level: {settings.LOG_LEVEL}")
    print(f"Log File: {settings.LOG_FILE}")
