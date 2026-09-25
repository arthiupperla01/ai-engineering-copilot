from fastapi import FastAPI

from backend.api.routes.health import router as health_router
from backend.config import settings

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "environment": settings.environment,
    }


app.include_router(health_router)