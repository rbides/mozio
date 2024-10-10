from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres2024@mozio-db:5432/postgres"

    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()