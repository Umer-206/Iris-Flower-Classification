import streamlit as st
import pandas as pd
import joblib

# Load scaler and best model (Logistic Regression in this case)
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/logistic_regression_model.pkl")

st.title("🌸 Iris Flower Classification App")
st.write("This app predicts the species of an Iris flower using a trained ML model.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.number_input("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.number_input("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.number_input("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict"):
    # Prepare input
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                              columns=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]
    species = ["Setosa", "Versicolor", "Virginica"][prediction]

    st.success(f"🌸 Predicted Species: **{species}**")
