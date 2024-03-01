# from pydantic.v1 import root_validator, BaseSettings
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    TOKEN: str
    TG_ID: int

    class Config:
        env_file = ".env"


settings = Settings()