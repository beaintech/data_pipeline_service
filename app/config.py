from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./pipeline.db"
    GOOGLE_SHEETS_ID: Optional[str] = None
    GOOGLE_SERVICE_ACCOUNT_FILE: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
