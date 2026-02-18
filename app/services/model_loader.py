from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

MODEL_NAME = "distilbert-base-uncased"

print("Loading model from HuggingFace...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained("ml/model")

model.eval()

print("Model ready")
