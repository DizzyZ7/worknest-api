from sqlalchemy.orm import Session
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate


def create_incident(db: Session, data: IncidentCreate) -> Incident:
    incident = Incident(title=data.title, status=data.status)
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


def get_incidents(db: Session):
    return db.query(Incident).all()
