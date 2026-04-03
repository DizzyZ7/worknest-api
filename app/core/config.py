from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "WorkNest API"
    version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"


settings = Settings()
