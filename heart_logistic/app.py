import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('heart.csv')


label_sex = LabelEncoder()
label_cp = LabelEncoder()
label_ecg = LabelEncoder()
label_angina = LabelEncoder()
label_slope = LabelEncoder()


df['Sex'] = label_sex.fit_transform(df['Sex'])
df['ChestPainType'] = label_cp.fit_transform(df['ChestPainType'])
df['RestingECG'] = label_ecg.fit_transform(df['RestingECG'])
df['ExerciseAngina'] = label_angina.fit_transform(df['ExerciseAngina'])
df['ST_Slope'] = label_slope.fit_transform(df['ST_Slope'])


X = df.iloc[:, :-1]
y = df.iloc[:, -1]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


model = LogisticRegression(class_weight='balanced', fit_intercept=True)
model.fit(X_scaled, y)

st.title("Heart Disease Prediction App")
st.markdown("Enter patient data to predict the likelihood of heart disease.")


age = st.slider("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ASY", "NAP", "ATA", "TA"])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 0, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak (ST depression)", -2.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


input_data = pd.DataFrame({
    'Age': [age],
    'Sex': label_sex.transform([sex]),
    'ChestPainType': label_cp.transform([chest_pain]),
    'RestingBP': [resting_bp],
    'Cholesterol': [cholesterol],
    'FastingBS': [fasting_bs],
    'RestingECG': label_ecg.transform([resting_ecg]),
    'MaxHR': [max_hr],
    'ExerciseAngina': label_angina.transform([exercise_angina]),
    'Oldpeak': [oldpeak],
    'ST_Slope': label_slope.transform([st_slope]),
})

input_scaled = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error(" the patient has 'Heart Disease'")
    else:
        st.success(" the patient does not have 'Heart Disease'")
