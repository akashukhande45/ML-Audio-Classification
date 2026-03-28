# ML Audio Classification System

## Description
This project is an audio classification system that predicts the category of sound from `.wav` files using Machine Learning.

It uses feature extraction (MFCC), a trained model, and a Flask API to provide real-time predictions. Based on the prediction, it also suggests a learning path.

---

##  Features
-  Classifies audio (.wav files)
-  Machine Learning prediction
-  MFCC feature extraction
-  Flask API integration
-  Learning path suggestion

---

## Technologies Used
- Python  
- NumPy  
- Librosa  
- Scikit-learn  
- Flask  

---

## 📂 Project Structure:
ML_task/
│
├── app.py
├── prediction.py
├── train.py
├── prepare_dataset.py
├── feature.py
├── learning_path.py
├── model.pkl
├── README.md

---

##  How to Run

### 1)Install dependencies

pip install numpy librosa scikit-learn flask

python prepare_dataset.py
python train.py
python app.py

## 📡 API Usage

- Method: POST  
- URL:
http://127.0.0.1:5000/predict

- Body:
  - form-data
  - key = file
  - type = File
  - value = .wav file

## 📊 Example Output


{
  "prediction": "dog",
  "learning_path": [
    "Learn Animals",
    "Identify Sounds",
    "Animal Quiz"
  ]
}

---

## Model Accuracy
- Accuracy: ~48%

## Note

The model file (model.pkl) is not uploaded due to GitHub file size limitations.

To run the project:
1. Run `prepare_dataset.py`
2. Run `train.py` to generate `model.pkl`
3. Then run `app.py`
