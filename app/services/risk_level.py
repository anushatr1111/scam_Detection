def risk_level(label: str, confidence: float, url_analysis: list):

    # base risk
    if label == "scam":
        risk_score = confidence * 100
    else:
        risk_score = (1 - confidence) * 100

    # URL risk override
    if url_analysis:
        risk_score = max(risk_score, max(u["risk_score"] for u in url_analysis))

    # classify level
    if risk_score >= 70:
        level = "dangerous"
    elif risk_score >= 40:
        level = "suspicious"
    else:
        level = "safe"

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": level
    }
