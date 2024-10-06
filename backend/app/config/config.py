import os
# from pydantic_settings import BaseSettings, SettingsConfigDict
import secrets

class Settings():
    DATABASE_URL: str = 'postgresql://localhost:5432/postgres'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60
    
    # model_config = SettingsConfigDict(
    #     env_file=".env", env_ignore_empty=True,s extra="ignore"
    # )
    
settings = Settings()
