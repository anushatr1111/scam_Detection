import re

URGENCY_WORDS = [
    "urgent","immediately","now","limited","hurry","act fast","suspend","blocked"
]

FINANCIAL_WORDS = [
    "bank","account","upi","refund","payment","prize","lottery","money","rs","debit","credit"
]

OTP_WORDS = [
    "otp","verify","verification","code","password"
]

def explain_text(text: str):
    text_lower = text.lower()
    reasons = []

    if any(word in text_lower for word in URGENCY_WORDS):
        reasons.append("Creates urgency pressure")

    if any(word in text_lower for word in FINANCIAL_WORDS):
        reasons.append("Mentions financial transaction")

    if any(word in text_lower for word in OTP_WORDS):
        reasons.append("Requests sensitive information")

    if re.search(r'http[s]?://|bit\.ly|tinyurl', text_lower):
        reasons.append("Contains suspicious link")

    if not reasons:
        reasons.append("General language pattern matched scam behavior")

    return reasons
