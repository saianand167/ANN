# --- RUN BUTTON HELPER (Do not edit) ---
import sys
import os
from streamlit.runtime import exists as st_exists
if __name__ == "__main__" and not st_exists():
    import streamlit.web.cli as stcli
    sys.argv = ["streamlit", "run", __file__]
    sys.exit(stcli.main())
# --------------------------------------

import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

# Load model and preprocessors
model = load_model("ann_model.h5")

with open("standardscaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("labelencoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

with open("onehotencoder.pkl", "rb") as f:
    onehot_encoder = pickle.load(f)

# Streamlit UI
st.title("Customer Churn Prediction By sairaj")
st.write("Enter the customer details below to predict whether they will churn.")

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
geography = st.selectbox("Geography", onehot_encoder.categories_[0])
gender = st.selectbox("Gender", label_encoder.classes_)
age = st.slider("Age", 18, 92, 40)
tenure = st.slider("Tenure", 0, 10, 3)
balance = st.number_input("Balance", min_value=0.0, value=60000.0)
num_of_products = st.slider("Number of Products", 1, 4, 2)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# Prediction
if st.button("Predict"):
    # Encode Gender using LabelEncoder
    gender_encoded = label_encoder.transform([gender])[0]

    # Encode Geography using OneHotEncoder
    geo_encoded = onehot_encoder.transform([[geography]]).toarray()

    # Build input array: all numeric features first
    input_data = np.array([[credit_score, gender_encoded, age, tenure, balance,
                            num_of_products, has_cr_card, is_active_member, estimated_salary]])

    # Append one-hot encoded geography columns
    input_data = np.concatenate([input_data, geo_encoded], axis=1)

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    pred_prob = prediction[0][0]

    st.write(f"### Churn Probability: {pred_prob:.2%}")
    if pred_prob > 0.5:
        st.error("⚠️ The customer is likely to churn!")
    else:
        st.success("✅ The customer is NOT likely to churn.")