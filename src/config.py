from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    API_V1_PREFIX: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()