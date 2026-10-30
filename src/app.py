from fastapi import APIRouter, FastAPI

from api.health.router import health_router

app = FastAPI(
    title="Chek",
    version="0.1.0",
)

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(router=health_router)

app.include_router(api_router)
