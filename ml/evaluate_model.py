import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc
import matplotlib.pyplot as plt

# Load model
MODEL_PATH = "ml/model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# Load dataset
df = pd.read_csv("ml/data/scam_dataset.csv")

texts = df["text"].tolist()
labels = [1 if l=="scam" else 0 for l in df["label"]]

predictions = []
probabilities = []

for text in texts:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=256)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
    prob_scam = probs[1].item()

    probabilities.append(prob_scam)
    predictions.append(1 if prob_scam > 0.5 else 0)

# ===== METRICS =====
print("\nClassification Report:\n")
print(classification_report(labels, predictions, target_names=["safe","scam"]))

# ===== CONFUSION MATRIX =====
cm = confusion_matrix(labels, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["safe","scam"])
disp.plot()
plt.title("Confusion Matrix")
plt.savefig("ml/confusion_matrix.png")
plt.close()

# ===== ROC CURVE =====
fpr, tpr, _ = roc_curve(labels, probabilities)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title(f"ROC Curve (AUC = {roc_auc:.2f})")
plt.savefig("ml/roc_curve.png")
plt.close()
