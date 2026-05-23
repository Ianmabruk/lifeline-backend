from pydantic import BaseModel, EmailStr, Field


class SummaryMetric(BaseModel):
    title: str
    value: str
    detail: str


class TrendPoint(BaseModel):
    name: str
    incoming: int
    resolved: int


class RiskPoint(BaseModel):
    name: str
    value: int


class HospitalReadinessPoint(BaseModel):
    region: str
    readiness: int
    rural: int


class Incident(BaseModel):
    name: str
    region: str
    coordinates: tuple[float, float]
    severity: str
    category: str
    status: str
    summary: str


class Hospital(BaseModel):
    name: str
    region: str
    level: str
    availability: str
    specialties: list[str]


class ContactRequest(BaseModel):
    organization: str = Field(min_length=2, max_length=120)
    email: EmailStr
    deployment_track: str = Field(min_length=2, max_length=120)
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(BaseModel):
    status: str
    reference: str
