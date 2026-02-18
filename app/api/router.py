from fastapi import APIRouter
from app.api.endpoints import health, debug

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(debug.router, tags=["Debug"])
from app.api.endpoints import health, debug, auth

api_router.include_router(auth.router)
from app.api.endpoints import scan
api_router.include_router(scan.router)
from app.api.endpoints import image_scan
api_router.include_router(image_scan.router)
from app.api.endpoints import monitor
api_router.include_router(monitor.router)
