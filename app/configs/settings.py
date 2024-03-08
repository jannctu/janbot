from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()
TEMP_DIR = Path(gettempdir())


class Settings(BaseSettings):

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    workers_count: int = 1
    reload: bool = False

    name: str = "janbot"
    app: str = "app"
    environment: str = "dev"

    openai_api_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_file_encoding="utf-8",
    )


settings = Settings()
