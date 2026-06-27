from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    kite_api_key: str
    kite_api_secret: str
    kite_redirect_url: HttpUrl
    kite_base_url: str = "https://api.kite.trade"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings: Settings = Settings()  # type: ignore[call-arg]
