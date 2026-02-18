from fastapi import APIRouter, UploadFile, File, Depends
from app.core.dependencies import get_current_user
from app.services.ocr_service import extract_text_from_image
from app.services.inference_engine import classify_text
import shutil
import uuid

router = APIRouter(prefix="/scan", tags=["Image Scan"])

@router.post("/image")
async def scan_image(file: UploadFile = File(...), user=Depends(get_current_user)):

    filename = f"temp_{uuid.uuid4().hex}.png"

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_image(filename)

    result = classify_text(text)

    return {
        "user": user.email,
        "extracted_text": text,
        "analysis": result
    }
