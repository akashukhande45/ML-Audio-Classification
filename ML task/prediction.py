import numpy as np
import joblib
from extract_features import extract_features

# Load model
model = joblib.load("model.pkl")

def predict_audio(file_path):
    features = extract_features(file_path)
    features = features.reshape(1, -1)

    prediction = model.predict(features)
    return prediction[0]