# STEP 8: Flask API for Placement Prediction
# ------------------------------------------

from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load trained model
with open("model/placement_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET"])
def home():
    return "AI-Based College Placement Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Convert input JSON to DataFrame
    input_df = pd.DataFrame([{
        'CGPA': data['CGPA'],
        'Skills': data['Skills'],
        'Internship': data['Internship'],
        'Backlogs': data['Backlogs']
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Return result
    return jsonify({
        "Placed": int(prediction),
        "Placement_Probability": round(probability * 100, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
