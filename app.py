from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([data['feature1'], data['feature2']]).reshape(1, -1)
    pred = model.predict(features)
    risk_map = {0: 'High', 1: 'Medium', 2: 'Low'}
    return jsonify({'risk_category': risk_map[pred]})

if __name__ == '__main__':
    app.run(debug=True)
