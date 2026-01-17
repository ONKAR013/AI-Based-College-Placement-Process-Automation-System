# 🎓 AI-Based College Placement Process Automation System

## 📌 Project Overview
The **AI-Based College Placement Process Automation System** is a Machine Learning–powered application designed to predict whether a student is likely to be placed based on academic and skill-related parameters. The system automates placement analysis, reducing manual effort and providing accurate, data-driven insights for students and placement cells.

This project demonstrates the practical application of **AI/ML**, **automation**, and **API development**, developed with assistance from **GitHub Copilot**.

---

## 🚀 Key Features
- Automated student placement prediction
- Probability-based placement result
- Machine Learning model using Random Forest
- Flask API for real-time predictions
- Excel-based batch automation
- Modular and scalable project structure

---

## 🧠 AI & Machine Learning Used
- **Algorithm:** Random Forest Classifier
- **Why Random Forest?**
  - High accuracy
  - Handles multiple features efficiently
  - Reduces overfitting

### Input Features
- CGPA
- Skills count
- Internship experience
- Number of backlogs

### Output
- Placement status (Placed / Not Placed)
- Placement probability (%)

---

## 🛠️ Technology Stack
- **Programming Language:** Python 3.x
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Flask
  - Pickle
- **Tools:**
  - VS Code
  - GitHub Copilot
  - Excel

---

## 📂 Project Structure
```
placement_ai/
│── data/
│   └── students.xlsx
│── model/
│   └── placement_model.pkl
│── train_model.py
│── app.py
│── automate.py
│── requirements.txt
│── README.md
```

---

## ⚙️ System Workflow
1. Load student dataset from Excel
2. Preprocess data and select features
3. Train ML model using Random Forest
4. Evaluate model accuracy
5. Save trained model
6. Predict placement for new students
7. Deploy model using Flask API
8. Automate predictions using Excel input

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model
```bash
python train_model.py
```

### 3️⃣ Run Flask API
```bash
python app.py
```
Open browser:
```
http://127.0.0.1:5000
```

### 4️⃣ Run Automation Script
```bash
python automate.py
```

---

## 📊 Sample Output
```
Student is likely to be PLACED
Placement Probability: 69.0%
```

---

## 📈 Results
- High accuracy achieved on training data
- Accurate prediction with probability score
- Fully automated placement analysis

---

## 🔮 Future Scope
- Use larger real-world datasets
- Add more student attributes (certifications, projects)
- Build a web dashboard
- Deploy on cloud platforms
- Integrate advanced ML models

---

## 🤖 Role of GitHub Copilot
GitHub Copilot was used to:
- Generate boilerplate ML and Flask code
- Assist in API design
- Improve code structure and readability
- Speed up development process

---

## 📚 References
- Scikit-learn Documentation
- Flask Documentation
- Python Official Docs
- Machine Learning Research Articles

---

## 👤 Author
**Onkar Kapgate**

---

## ⭐ Conclusion
This project showcases how Artificial Intelligence and automation can enhance the college placement process by providing fast, accurate, and data-driven predictions. It highlights the real-world impact of AI in the education domain.

---

⭐ *If you found this project useful, please star the repository!*
