from fastapi import FastAPI
from app.core.settings_prod import settings
from app.api.v1.router import router as base_router
from app.api.v1.incidents import router as incidents_router

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(base_router, prefix=settings.API_V1_PREFIX)
app.include_router(incidents_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
def root():
    return {"service": settings.APP_NAME}
