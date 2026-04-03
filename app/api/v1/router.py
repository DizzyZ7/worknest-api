from fastapi import APIRouter
from app.api.v1.incidents import router as incidents_router

router = APIRouter()


@router.get("/info")
def info():
    return {"service": "WorkNest API", "status": "running"}


router.include_router(incidents_router)
