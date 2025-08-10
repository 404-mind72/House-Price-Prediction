import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model & data
model = joblib.load("model.pkl")
df = pd.read_csv("House Price India.csv")

# Judul
st.title("🏠 House Price Prediction App")
st.markdown("This app uses machine learning for prediction house price with given features of the house. For using this app you can enter the input from this UOI and the use predict button.")

st.markdown("---")

# Layout input
col1, col2 = st.columns(2)
with col1:
    bedrooms = st.slider("🛏 Number of bedrooms", 0, 10, 3)
    bathrooms = st.slider("🛁 Number of bathrooms", 0, 10, 2)
    condition = st.slider("🏠 Condition", 1, 5, 3)
with col2:
    livingarea = st.number_input("📐 Living area (sq ft)", min_value=0, value=2000, step=100)
    numberofschools = st.slider("🏫 Schools nearby", 0, 20, 5)

st.markdown("---")

# Input array
x = [[bedrooms, bathrooms, livingarea, condition, numberofschools]]

# Predict
if st.button("🔮 Predict Price"):
    x_array = np.array(x)
    prediction = model.predict(x_array)[0]
    st.success(f"💰 Estimated Price: **{prediction:,.2f}**")
else:
    st.info("Enter data and click *Predict Price* to see the result.")

st.markdown("---")

