import os


class Settings:
    APP_NAME = os.getenv("APP_NAME", "WorkNest API")
    APP_VERSION = os.getenv("APP_VERSION", "0.2.0")
    API_V1_PREFIX = os.getenv("API_V1_PREFIX", "/api/v1")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")


settings = Settings()
