from fastapi import APIRouter
from .routes import healthcheck

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["Health Check"])
