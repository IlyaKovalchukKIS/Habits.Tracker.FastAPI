import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_HOST: str = os.getenv("APP_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_ECHO: bool = bool(os.getenv("DB_ECHO"))
    REDIS_USER: str = os.getenv("REDIS_USER")
    REDIS_PASSWORD: str = os.getenv("REDIS_USER_PASSWORD")
    REDIS_PORT: str = os.getenv("REDIS_PORT")
    AUTH_VERIFY_KEY: str = os.getenv("AUTH_VERIFY_KEY")
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD")

    @property
    def DATABASE_URL_redis(self):
        return (
            f"redis://default:{self.REDIS_PASSWORD}@{self.DB_HOST}:{self.REDIS_PORT}/1"
        )

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/postgres"

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/postgres"


settings = Settings()
