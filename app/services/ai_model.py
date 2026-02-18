from transformers import pipeline

# Load once (important — do NOT load per request)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_scam(text: str):
    result = classifier(text[:512])[0]

    label = result["label"]
    score = result["score"]

    # reinterpret sentiment as scam probability
    if label == "NEGATIVE":
        scam_probability = score
    else:
        scam_probability = 1 - score

    scam_probability = round(float(scam_probability), 3)

    return {
        "label": "scam" if scam_probability > 0.6 else "safe",
        "confidence": scam_probability,
        "model": "distilbert-sentiment-v1"
    }
