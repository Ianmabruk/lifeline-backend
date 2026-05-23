from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router


app = FastAPI(
    title="LIFELINE EARTH API",
    description="Humanitarian operations API for emergency response, healthcare, disaster intelligence, and public safety workflows.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "lifeline-earth-backend"}