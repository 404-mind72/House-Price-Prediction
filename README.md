# 🏠 House Price Prediction
## 📌 Project Description
This project is a house price prediction application in India using machine learning. The model is trained using a public dataset from Kaggle containing various house features such as the number of bedrooms, bathrooms, building area, condition, and number of nearby schools.

## 📂 Dataset
Dataset: House Price India.csv (source: Kaggle)
- Key features used:
- bedrooms – number of bedrooms
- bathrooms – number of bathrooms
- livingarea – building area (sq ft)
- condition – condition of the house (scale 1–5)
- numberofschools – number of schools near the house

Prediction target:
House price (in dataset currency)

## ⚙️ Methodology
#### 1. Data Preprocessing
- Selecting relevant features from the dataset
- Normalization/Standardization if necessary (depending on the model)
#### 2. Modeling
- Machine Learning models are saved in the model.pkl file (e.g., using Random Forest Regressor or other regression algorithms)
#### 3. Model Evaluation
- Using regression evaluation metrics such as R² Score, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
#### 4. Deployment
- The model is integrated with the Streamlit application for real-time house price prediction.

## 📦 Library
- pandas
- numpy
- scikit-learn
- joblib
- streamlit
- matplotlib
