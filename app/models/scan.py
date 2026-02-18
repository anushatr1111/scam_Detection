from pydantic import BaseModel, Field

class TextScanRequest(BaseModel):
    text: str = Field(..., min_length=5, max_length=2000)
