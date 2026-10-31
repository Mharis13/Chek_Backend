from fastapi import APIRouter, FastAPI

from api.health.router import health_router

app = FastAPI(
    title="Chek",
    version="0.1.0",
)

api_router = APIRouter(prefix="/api/v1")


app.include_router(health_router)
app.include_router(api_router)
