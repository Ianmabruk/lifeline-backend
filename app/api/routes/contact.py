from uuid import uuid4

from fastapi import APIRouter

from app.schemas import ContactRequest, ContactResponse


router = APIRouter()


@router.post("/contact", response_model=ContactResponse)
def create_contact_request(payload: ContactRequest) -> ContactResponse:
    reference = f"LE-{uuid4().hex[:10].upper()}"
    return ContactResponse(status="queued", reference=reference)