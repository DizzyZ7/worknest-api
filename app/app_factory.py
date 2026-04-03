from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.version)

    @app.get("/")
    def read_root():
        return {"message": f"Welcome to {settings.app_name}"}

    @app.get("/health")
    def healthcheck():
        return {"status": "ok", "version": settings.version}

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    return app
