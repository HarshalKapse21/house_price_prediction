#Bengaluru House Price Prediction

A Machine Learning web application that predicts house prices in Bengaluru based on user inputs like location, square feet, number of bedrooms, and bathrooms.

🚀 Built using Python, Scikit-learn, and Streamlit

##Live Demo

 **Try the App:**  
[https://housepricepredictiongit-tjcgpklydgdkqg3uicphrk.streamlit.app/](https://housepricepredictiongit-tjcgpklydgdkqg3uicphrk.streamlit.app/)

##  Problem Statement

Real estate prices in Bengaluru vary significantly based on location, size, and amenities.  
This project builds a Machine Learning model to **predict house prices accurately** based on key features.

##  Key Features

- End-to-End ML Pipeline  
- Data Cleaning & Feature Engineering  
- Outlier Detection & Removal  
- One-Hot Encoding for Locations  
- Linear Regression Model  
- Interactive Streamlit Web App  
- Fast Real-Time Predictions  

##  Tech Stack

| Category | Tools |
|---------|------|
| Language | Python |
| ML | Scikit-learn |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Model Saving | Joblib |



##  Project Structure

house_price_prediction/
│
├── BHP.ipynb # Model training notebook
├── app.py # Streamlit application
├── model.joblib # Trained ML model
├── columns.json # Feature columns
├── requirements.txt # Dependencies
└── README.md # Documentation


---

##  How the App Works

1. User selects location, sqft, bath, and BHK  
2. App converts inputs into feature vector  
3. Trained model predicts price  
4. Result shown instantly in UI  

The Streamlit app loads the model and columns efficiently using caching for better performance. :contentReference[oaicite:0]{index=0}

##  Run Locally

### Clone Repository

git clone https://github.com/HarshalKapse21/house_price_prediction.git
cd house_price_prediction

## Install Dependencies

pip install -r requirements.txt

## Run Streamlit App

streamlit run app.py

## Model Information

- Algorithm: Linear Regression
- Target: House Price (Lakhs)
### Features Used:
- total_sqft
- bath
- bhk
- location (one-hot encoded)
- Location features are dynamically loaded from the columns configuration. 
- columns

## Future Improvements

- Try XGBoost / Random Forest
- Improve UI/UX
- Add more dataset samples
-  Docker containerization
- CI/CD pipeline

## Author

- Harshal Kapse
- Aspiring Data Analyst | ML Enthusiast
- LinkedIn: ((https://www.linkedin.com/in/harshal-kapse-0b4331260/))
