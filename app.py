import streamlit as st
import joblib
import numpy as np

model = joblib.load("crop_model.pkl")

st.title("🌾 Crop Recommendation System")

N = st.number_input("Nitrogen (N)", 0, 200)
P = st.number_input("Phosphorus (P)", 0, 200)
K = st.number_input("Potassium (K)", 0, 200)
temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
ph = st.slider("pH Level", 0.0, 14.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 100.0)

if st.button("Recommend Crop"):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)[0]
    st.success(f"🌱 Recommended Crop: **{prediction}**")
 
