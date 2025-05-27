# ❤️ Heart Disease Prediction using Machine Learning

This is a machine learning-based web application that predicts the risk of heart disease based on various health parameters. The model is trained using Python and deployed using **Streamlit** for easy access and interaction. The application is **live and accessible online**.

---

## 🚀 Live Demo

👉 [Click here to try the live app](https://your-deployment-link-here)

> ⚠️ Replace the above link with your actual deployment URL.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Model Details](#-model-details)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technologies Used](#-technologies-used)
- [Available Files](#-available-files)
- [Contact](#-contact)
- [License](#-license)

---

## 📊 Overview

Heart disease is a major public health concern, and early detection is vital for prevention and treatment. This machine learning model analyzes key indicators to determine the likelihood of heart disease in a patient.

The model takes input features like:
- Age
- Sex
- Chest Pain Type
- Blood Pressure
- Cholesterol
- Blood Sugar
- Resting ECG
- Max Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope, Number of Major Vessels, Thalassemia, etc.

It predicts:
- `0` – No Heart Disease
- `1` – Likely to Have Heart Disease

---

## 🧠 Model Details

- **Programming Language:** Python  
- **Machine Learning Algorithm:** (e.g., Logistic Regression / Random Forest / SVM)  
- **Model Format:** `.sav` (Serialized using `joblib` or `pickle`)  
- **Deployment Platform:** Streamlit

---

## 📁 Project Structure

**heart-disease-prediction**/
│
├── app.py # Main Streamlit app
├── heart_disease_model.sav # Pre-trained machine learning model
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## 💻 Installation

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
2. **Install dependencies**
   pip install -r requirements.txt
3. **Run the app**
   streamlit run app.py

**🔧 Technologies Used**
-Python

-Scikit-learn

-Pandas & NumPy

-Streamlit

-Matplotlib / Seaborn (optional for visualization)

-Pickle

**📦 Available Files**
app.py – Streamlit frontend that takes user input and displays the prediction.

heart_disease_model.sav – Trained ML model file.

requirements.txt – List of required Python libraries.

README.md – Documentation file.
