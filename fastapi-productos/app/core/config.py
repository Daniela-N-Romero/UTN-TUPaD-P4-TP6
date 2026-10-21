from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Productos & Categorías"
    DATABASE_URL: str = "sqlite:///database.db"

    class Config:
        env_file = ".env"

settings = Settings()