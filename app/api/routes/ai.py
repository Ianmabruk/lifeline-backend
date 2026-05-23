from fastapi import APIRouter

from app.data import AI_RECOMMENDATIONS


router = APIRouter()


@router.get("/recommendations")
def get_recommendations():
    return {"items": AI_RECOMMENDATIONS}