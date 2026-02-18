import torch
from app.services.model_loader import tokenizer, model
from app.services.explainer import explain_text
from app.services.url_scanner import analyze_url
from app.services.risk_level import risk_level

LABELS = ["safe", "scam"]

def classify_text(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
    confidence, predicted = torch.max(probs, dim=0)

    label = LABELS[int(predicted)]
    confidence = round(float(confidence), 3)

    # NLP reasons
    reasons = explain_text(text) if label == "scam" else []

    # URL analysis
    url_results = analyze_url(text) if text else []

    # If malicious URL detected → override
    if url_results and max(u["risk_score"] for u in url_results) > 70:
        label = "scam"
        reasons.append("Malicious link detected")
    risk = risk_level(label, confidence, url_results)

    return {
        "label": label,
        "confidence": confidence,
        "model": "distilbert-custom-architecture",
        "reasons": reasons,
        "url_analysis": url_results,
        "risk": risk
    }
