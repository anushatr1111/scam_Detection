import re
from urllib.parse import urlparse

SUSPICIOUS_TLDS = ["xyz","top","click","work","gq","tk"]
PHISHING_WORDS = ["verify","login","secure","account","update","bank","kyc","wallet"]

def analyze_url(text: str):
    urls = re.findall(r'(https?://\S+)', text.lower())

    results = []

    for url in urls:
        parsed = urlparse(url)
        domain = parsed.netloc

        risk = 0
        reasons = []

        # shortened links
        if any(short in domain for short in ["bit.ly","tinyurl","t.co"]):
            risk += 40
            reasons.append("Shortened URL hides destination")

        # suspicious tld
        if domain.split(".")[-1] in SUSPICIOUS_TLDS:
            risk += 30
            reasons.append("Suspicious domain extension")

        # phishing words
        if any(word in domain for word in PHISHING_WORDS):
            risk += 30
            reasons.append("Impersonates service")

        # ip address
        if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
            risk += 50
            reasons.append("Uses raw IP address")

        results.append({
            "url": url,
            "risk_score": min(risk,100),
            "reasons": reasons
        })

    return results
