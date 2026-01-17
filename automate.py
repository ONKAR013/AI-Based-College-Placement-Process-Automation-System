# STEP 9: Python Automation (Excel → AI Model → Output)
# ----------------------------------------------------

import pandas as pd
import pickle

# Load trained model
with open("model/placement_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Excel file
df = pd.read_excel("data/students.xlsx")

print("\n--- Automated Placement Prediction Results ---\n")

# Iterate through each student
for index, row in df.iterrows():
    input_df = pd.DataFrame([{
        'CGPA': row['CGPA'],
        'Skills': row['Skills'],
        'Internship': row['Internship'],
        'Backlogs': row['Backlogs']
    }])

    # Predict placement
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Display result
    status = "PLACED" if prediction == 1 else "NOT PLACED"

    print(f"Student: {row['StudentName']}")
    print(f"Status: {status}")
    print(f"Placement Probability: {round(probability * 100, 2)}%")
    print("-" * 40)
