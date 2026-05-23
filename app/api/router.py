from fastapi import APIRouter

from app.api.routes import ai, contact, dashboard, incidents


api_router = APIRouter()
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(incidents.router, tags=["operations"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(contact.router, tags=["contact"])