"""Main entry point for the Music Matcher API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Allowed origins for CORS
ALLOWED_ORIGINS = ["http://localhost:5173"]

app: FastAPI = FastAPI(title="Music Matcher API")

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def health_check() -> dict[str, str]:
    """Health-check endpoint returning API status."""
    return {"status": "ok"}
