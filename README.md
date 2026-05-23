# LIFELINE EARTH Backend

LIFELINE EARTH backend is a FastAPI service that provides mock-ready API surfaces for the humanitarian platform frontend. It is structured to support emergency operations, healthcare records, disaster intelligence, AI recommendations, and institutional contact workflows.

## Stack

- FastAPI
- Uvicorn
- Pydantic v2

## Features

- Health and readiness endpoint
- Dashboard summary and trend endpoints
- Global incident and map data endpoints
- Hospital network endpoint
- AI recommendation endpoint
- Contact intake endpoint

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Routes

- `GET /health`
- `GET /api/v1/dashboard/summary`
- `GET /api/v1/dashboard/trends`
- `GET /api/v1/dashboard/risk-distribution`
- `GET /api/v1/dashboard/hospital-readiness`
- `GET /api/v1/incidents`
- `GET /api/v1/map/incidents`
- `GET /api/v1/hospitals`
- `GET /api/v1/ai/recommendations`
- `POST /api/v1/contact`