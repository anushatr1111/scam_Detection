from fastapi import APIRouter, Depends
from app.models.scan import TextScanRequest
from app.services.inference_engine import classify_text
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/monitor", tags=["Protection"])

@router.post("/message")
def monitor_message(data: TextScanRequest, user=Depends(get_current_user)):

    analysis = classify_text(data.text)

    level = analysis["risk"]["risk_level"]

    if level == "dangerous":
        action = "block"
    elif level == "suspicious":
        action = "warn"
    else:
        action = "allow"

    return {
        "message": data.text,
        "decision": action,
        "risk": analysis["risk"],
        "reasons": analysis["reasons"]
    }
