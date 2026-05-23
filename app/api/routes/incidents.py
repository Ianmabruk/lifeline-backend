from fastapi import APIRouter

from app.data import HOSPITALS, INCIDENTS


router = APIRouter()


@router.get("/incidents")
def get_incidents():
    return INCIDENTS


@router.get("/map/incidents")
def get_map_incidents():
    return INCIDENTS


@router.get("/hospitals")
def get_hospitals():
    return HOSPITALS