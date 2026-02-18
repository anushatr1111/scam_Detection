from fastapi import APIRouter
from app.models.response import APIResponse

router = APIRouter()

@router.get("/debug")
def debug():
    return APIResponse(success=True, message="Debug route working")
