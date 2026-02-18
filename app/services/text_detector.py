import re

SCAM_KEYWORDS = [
    "urgent",
    "lottery",
    "winner",
    "free money",
    "click here",
    "verify otp",
    "bank account blocked",
    "limited offer",
    "act now",
    "password reset",
    "claim reward",
]

def detect_scam(text: str):
    text_lower = text.lower()

    matches = [kw for kw in SCAM_KEYWORDS if kw in text_lower]

    url_found = bool(re.search(r'https?://\S+', text_lower))

    score = len(matches) * 15 + (20 if url_found else 0)
    score = min(score, 95)

    label = "scam" if score >= 40 else "safe"

    return {
        "label": label,
        "confidence": score,
        "matched_keywords": matches,
        "contains_link": url_found
    }
