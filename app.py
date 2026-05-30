import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset
df = pd.read_csv("Hyderbad_House_price.csv")
st.title("House Price Prediction System")
st.subheader("Dataset Preview")
st.write(df.head())
# Analytics
st.subheader("Location-wise Average Prices")
location_data = df.groupby("location")["price(L)"].mean()
fig, ax = plt.subplots(figsize=(10,5))
location_data.sort_values(ascending=False).head(10).plot(
    kind='bar',
    ax=ax)
st.pyplot(fig)
# Inputs
area = st.number_input("Area in Sqft", value=1500)
rate = st.number_input("Rate Per Sqft", value=6000)
# Prediction button
if st.button("Predict Price"):
    predicted_price = (area * rate) / 100000
    st.success(f"Predicted Price: ₹ {predicted_price:.2f} Lakhs")