from flask import Flask, request, jsonify
from prediction import predict_audio
from learning_path import get_learning_path
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']

        file_path = "temp.wav"
        file.save(file_path)

        # Predict
        label = predict_audio(file_path)

        # Get learning path
        path = get_learning_path(label)

        # Optional: delete temp file
        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({
            "prediction": label,
            "learning_path": path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)