import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

# Load model and preprocessors
st.title("Customer Churn Prediction By sairaj")
st.write("Enter about your self below to predict whether you will churn.")
name=st.text_input("Enter your name",value="sairaj") 
