# ============================================================
# AI-Based College Placement Process Automation System
# STEP 2 to STEP 7 (Single Integrated Script)
# GitHub Copilot–Assisted Development
# ============================================================

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------------------------------------
# STEP 2: Load & Understand Dataset
# ------------------------------------------------------------

df = pd.read_excel("data/students.xlsx")

print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------------------------
# STEP 3: Data Preprocessing & Feature Selection
# ------------------------------------------------------------

# Select relevant features (exclude name & email)
X = df[['CGPA', 'Skills', 'Internship', 'Backlogs']]

# Target variable
y = df['Placed']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# ------------------------------------------------------------
# STEP 4: Model Selection & Training
# ------------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
print("\nModel training completed successfully")

# ------------------------------------------------------------
# STEP 5: Model Evaluation
# ------------------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------------------------------------
# STEP 6: Prediction for New Student
# ------------------------------------------------------------

new_student = pd.DataFrame([{
    'CGPA': 7.8,
    'Skills': 4,
    'Internship': 1,
    'Backlogs': 0
}])

prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0][1]

print("\nNew Student Prediction:")
if prediction == 1:
    print("Student is likely to be PLACED")
else:
    print("Student is likely to be NOT PLACED")

print("Placement Probability:", round(probability * 100, 2), "%")

# ------------------------------------------------------------
# STEP 7: Save & Reload Model
# ------------------------------------------------------------

# Save model
with open("model/placement_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully")

# Load model
with open("model/placement_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully")

# Verify loaded model
test_prediction = loaded_model.predict(new_student)[0]
print("Verification using loaded model:",
      "Placed" if test_prediction == 1 else "Not Placed")
