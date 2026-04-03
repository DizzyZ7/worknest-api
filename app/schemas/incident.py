from pydantic import BaseModel, Field


class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    status: str = Field(default="open", max_length=50)


class IncidentRead(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        from_attributes = True
