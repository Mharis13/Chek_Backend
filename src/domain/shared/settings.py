from constants import DOTENV_PATH
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV_PATH, env_file_encoding="utf-8")

    database_url: str | None = Field(default=None)
