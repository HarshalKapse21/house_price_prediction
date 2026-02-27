import streamlit as st
import json
import joblib
import numpy as np

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Bengaluru House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Load Artifacts
# -----------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("model.joblib")
    with open("columns.json", "r") as f:
        data_columns = json.load(f)["data_columns"]
    return model, data_columns


model, data_columns = load_artifacts()
locations = sorted(data_columns[3:])

# -----------------------------
# Header
# -----------------------------
st.title("🏠 Bengaluru House Price Prediction")
st.markdown("Predict apartment prices instantly using a trained ML model.")
st.divider()

# -----------------------------
# Sidebar Info
# -----------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "This app predicts Bengaluru house prices based on square footage, "
        "number of bathrooms, BHK, and location."
    )
    st.success("Model Loaded Successfully")

# -----------------------------
# User Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("📍 Location", locations)
    sqft = st.number_input(
        "📐 Total Square Feet",
        min_value=300,
        max_value=10000,
        value=1000,
        step=50
    )

with col2:
    bath = st.number_input("🛁 Bathrooms", 1, 10, 2)
    bhk = st.number_input("🛏️ BHK", 1, 10, 2)


# -----------------------------
# Prediction Function
# -----------------------------
def predict_price(location, sqft, bath, bhk):
    location = location.lower()
    try:
        loc_index = data_columns.index(location)
    except ValueError:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    prediction = model.predict([x])[0]
    return round(prediction, 2)


# -----------------------------
# Predict Button
# -----------------------------
st.divider()

if st.button("🔮 Predict Price", use_container_width=True):
    with st.spinner("Calculating best price..."):
        try:
            price = predict_price(location, sqft, bath, bhk)
            st.success(f"💰 Estimated Price: ₹ {price} Lakhs")

            st.metric("Predicted Price (Lakhs)", price)

        except Exception as e:
            st.error("⚠️ Prediction failed. Please check inputs.")
            st.exception(e)


# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Built with using Streamlit | ML Model: Bengaluru Housing")
