from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./pipeline.db"
    GOOGLE_SHEETS_ID: str | None = None
    GOOGLE_SERVICE_ACCOUNT_FILE: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
