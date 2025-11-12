import streamlit as st
import pandas as pd
import joblib
import lightgbm as lgb
from geopy.distance import geodesic

model = joblib.load('fraud_detection_model.jb')
encoders = joblib.load('label_encoders.jb')

def haversine_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).km

st.title("Credit Card Fraud Detection System")
st.write("Enter transaction details to predict if it's fraudulent.")

merchant = st.text_input("Merchant Name")
category = st.text_input("Category")
amount = st.number_input("Transaction Amount", min_value=0.0, format="%.2f")
lat = st.number_input("Transaction Latitude", format="%.2f")
lon = st.number_input("Transaction Longitude", format="%.2f")
merchant_lat = st.number_input("Merchant Latitude", format="%.2f")
merchant_lon = st.number_input("Merchant Longitude", format="%.2f")
hour = st.slider("Transaction Hour", 0, 23, 12)
day = st.slider("Transaction Day", 1, 31, 15)  
month = st.slider("Transaction Month", 1, 12, 6)
gender = st.selectbox("Cardholder Gender", ["Male", "Female"])
cc_num = st.text_input("Cardholder Credit Card Number")

distance = haversine_distance(lat, lon, merchant_lat, merchant_lon)

if st.button("Predict Fraud"):
    if merchant and category and cc_num:
        input_data = pd.DataFrame({
            'merchant': [merchant],
            'category': [category],
            'amount': [amount],
            'distance': [distance],
            'hour': [hour],
            'day': [day],
            'month': [month],
            'gender': [gender], 
            'cc_num': [cc_num]
        })
        categorical_features = ['merchant', 'category', 'gender']
        for feature in categorical_features:
            try:
                input_data[feature] = encoders[feature].transform(input_data[feature])
            except ValueError:
                input_data[feature] = -1

        input_data['cc_num'] = input_data['cc_num'].apply(lambda x: hash(x) % 10**2)
        prediction = model.predict(input_data)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
        st.success(f"Prediction: {result}")
    else:
        st.error("Please fill in all required fields.")