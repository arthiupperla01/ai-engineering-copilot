from fastapi import FastAPI

from backend.config import settings

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "environment": settings.environment,
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}