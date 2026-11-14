
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool
    database_url: str
    llm_provider: str
    status :str
    gemini_api_key: SecretStr
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  
    )

settings = Settings()