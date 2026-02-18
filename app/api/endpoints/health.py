from fastapi import APIRouter
from app.models.response import APIResponse
from app.core.config import settings

router = APIRouter()

@router.get("/health", response_model=APIResponse)
def health_check():
    return APIResponse(
        success=True,
        message="API Running",
        data={
            "app": settings.APP_NAME,
            "version": settings.APP_VERSION
        }
    )
