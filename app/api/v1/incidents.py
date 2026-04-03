from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, Base, engine
from app.models.incident import Incident

router = APIRouter()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/incidents")
def create_incident(title: str, db: Session = Depends(get_db)):
    incident = Incident(title=title)
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


@router.get("/incidents")
def list_incidents(db: Session = Depends(get_db)):
    return db.query(Incident).all()
