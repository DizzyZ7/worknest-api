from fastapi import FastAPI
from app.core.settings_prod import settings
from app.api.v1.router import router
from app.db.session import engine, Base


def create_app():
    app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

    @app.on_event("startup")
    def startup():
        Base.metadata.create_all(bind=engine)

    app.include_router(router, prefix=settings.API_V1_PREFIX)

    return app
