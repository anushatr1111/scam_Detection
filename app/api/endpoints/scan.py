from fastapi import APIRouter, Depends
from app.models.scan import TextScanRequest
from app.core.dependencies import get_current_user
from app.services.inference_engine import classify_text

router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/text")
def scan_text(data: TextScanRequest, user=Depends(get_current_user)):
    result = classify_text(data.text)

    return {
        "user": user.email,
        "analysis": result
    }
