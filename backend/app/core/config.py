
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool
    database_url: str
    llm_provider: str
    status :str



    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignores extra env vars not defined in the model
    )

settings = Settings()