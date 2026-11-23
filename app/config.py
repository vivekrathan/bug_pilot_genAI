
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.5-flash-lite"

    embedding_model: str = "gemini-embedding-001"

    chroma_path: str = "./chroma_db"
    collection_name: str = "bug_knowledge_gemini"

    top_k: int = 4

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()


