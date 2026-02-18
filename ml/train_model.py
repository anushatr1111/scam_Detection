import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import torch

# Load dataset
df = pd.read_csv("C:\\Users\\Lenovo\\Scam_detetction\\backend\\ml\\data\\indian_upi_scam_dataset.csv")

# Convert labels
df["label"] = df["label"].map({"safe": 0, "scam": 1})

dataset = Dataset.from_pandas(df)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(tokenize)

dataset = dataset.train_test_split(test_size=0.2)

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

# Training config (CPU friendly)
training_args = TrainingArguments(
    output_dir="ml/model",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=4,
    logging_steps=5,
    save_strategy="epoch",
    eval_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()

trainer.save_model("ml/model")
tokenizer.save_pretrained("ml/model")
