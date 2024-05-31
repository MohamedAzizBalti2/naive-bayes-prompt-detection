import pickle
from pathlib import Path


__version__ = "3"

BASE_DIR = Path(__file__).resolve(strict=True).parent

classes = ['PII', 'benign', 'injection', 'jailbreak']

with open(f"{BASE_DIR}/pipeline_model_final_version"+".pkl", "rb") as f:
    model = pickle.load(f)

def predict_pipeline(text):
    predicted_probabilities = model.predict_proba([text])[0]
    class_probabilities = {cls: prob for cls, prob in zip(classes, predicted_probabilities)}
    return class_probabilities