from fastapi import APIRouter

from app.data import HOSPITAL_READINESS, RESPONSE_TREND, RISK_DISTRIBUTION, SUMMARY_METRICS


router = APIRouter()


@router.get("/summary")
def get_summary():
    return SUMMARY_METRICS


@router.get("/trends")
def get_trends():
    return RESPONSE_TREND


@router.get("/risk-distribution")
def get_risk_distribution():
    return RISK_DISTRIBUTION


@router.get("/hospital-readiness")
def get_hospital_readiness():
    return HOSPITAL_READINESS