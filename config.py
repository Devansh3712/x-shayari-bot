from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    API_KEY: str
    API_SECRET_KEY: str
    ACCESS_TOKEN: str
    ACCESS_TOKEN_SECRET: str


env = Settings()
