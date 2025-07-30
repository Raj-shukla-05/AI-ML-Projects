import streamlit as st
import numpy as np
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import os

# Set up Streamlit page config
st.set_page_config(page_title="Disease Risk Predictor", layout="centered")

# Load trained model
model = pickle.load(open("models/best_model.pkl", "rb"))

# App Title
st.title("🧠 Early Disease Risk Prediction")
st.markdown("This app predicts the risk of **diabetes** using a machine learning model trained on the PIMA dataset.")

# Create tab layout
tab1, tab2 = st.tabs(["📊 Prediction", "🧠 Model Explainability"])

# ------------------ Tab 1: Prediction ------------------ #
with tab1:
    st.subheader("Enter Patient Information")

    # Input fields
    Pregnancies = st.number_input('Pregnancies', 0, 20, step=1)
    Glucose = st.slider('Glucose Level', 50, 200)
    BloodPressure = st.slider('Blood Pressure', 40, 120)
    SkinThickness = st.slider('Skin Thickness', 0, 100)
    Insulin = st.slider('Insulin Level', 0, 900)
    BMI = st.slider('BMI', 10.0, 70.0)
    DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', 0.0, 2.5)
    Age = st.slider('Age', 10, 100)

    if st.button('Predict Risk'):
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = model.predict(input_data)
        result = '🟥 High Risk of Diabetes' if prediction[0] == 1 else '🟩 Low Risk of Diabetes'
        st.success(f"Prediction: {result}")

# ------------------ Tab 2: Explainability ------------------ #
with tab2:
    st.subheader("Model Explainability using SHAP")

    shap_summary = "visuals/explainability/shap_summary_plot.png"
    shap_bar = "visuals/explainability/shap_feature_importance.png"

    if os.path.exists(shap_summary) and os.path.exists(shap_bar):
        st.image(shap_summary, caption="SHAP Summary Plot", use_column_width=True)
        st.image(shap_bar, caption="SHAP Feature Importance", use_column_width=True)
    else:
        st.warning("SHAP plots not found. Please generate them using shap_explainability.ipynb")
