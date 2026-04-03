from fastapi import APIRouter

router = APIRouter()

@router.get("/incidents-v2")
def list_incidents():
    return {"status": "v2"}
