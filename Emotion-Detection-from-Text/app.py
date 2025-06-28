import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page title
st.title("🧠 Emotion Detection from Text")

# User input
user_input = st.text_area("Enter a sentence to detect emotion")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Preprocess input
        input_vector = vectorizer.transform([user_input.lower()])
        prediction = model.predict(input_vector)[0]

        # Output
        st.success(f"🎯 Predicted Emotion: **{prediction.upper()}**")
