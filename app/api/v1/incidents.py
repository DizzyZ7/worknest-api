from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.incident import IncidentCreate, IncidentRead
from app.services.incident_service import create_incident, get_incidents

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/incidents", response_model=IncidentRead)
def create_incident_endpoint(data: IncidentCreate, db: Session = Depends(get_db)):
    return create_incident(db, data)


@router.get("/incidents", response_model=list[IncidentRead])
def list_incidents_endpoint(db: Session = Depends(get_db)):
    return get_incidents(db)
