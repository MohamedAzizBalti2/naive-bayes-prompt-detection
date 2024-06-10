import pickle
from pathlib import Path

import numpy as np  # Add this import statement

__version__ = "3"

BASE_DIR = Path(__file__).resolve(strict=True).parent

classes = ['benign', 'injection', 'jailbreak']

with open(f"{BASE_DIR}/pipeline_model_final_version"+".pkl", "rb") as f:
    model = pickle.load(f)

def predict_pipeline(text):
    predicted_probabilities = model.predict_proba([text])[0]
    
    # Convert numpy.float32 objects to Python floats
    predicted_probabilities = [float(prob) for prob in predicted_probabilities]

    class_probabilities = {cls: prob for cls, prob in zip(classes, predicted_probabilities)}
    print(class_probabilities)
    return class_probabilities
