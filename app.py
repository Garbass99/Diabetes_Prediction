import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('diabetismodel.pkl')

# Set app title
st.title('Diabetes Prediction App')

# Add sidebar with information
st.sidebar.header('Patient Data')
st.sidebar.info('Enter the patient details to predict diabetes risk')

# Create input fields for each feature
pregnancies = st.slider('Pregnancies', 0, 17, 1)
glucose = st.slider('Glucose Level', 0, 200, 100)
blood_pressure = st.slider('Blood Pressure (mm Hg)', 0, 122, 70)
skin_thickness = st.slider('Skin Thickness (mm)', 0, 99, 20)
insulin = st.slider('Insulin Level (mu U/ml)', 0, 846, 80)
bmi = st.slider('BMI', 0.0, 67.1, 25.0)
diabetes_pedigree = st.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.5)
age = st.slider('Age', 21, 81, 30)

# Create a dataframe from the inputs
input_data = pd.DataFrame({
    'Pregnancies': [pregnancies],
    'Glucose': [glucose],
    'BloodPressure': [blood_pressure],
    'SkinThickness': [skin_thickness],
    'Insulin': [insulin],
    'BMI': [bmi],
    'DiabetesPedigreeFunction': [diabetes_pedigree],
    'Age': [age]
})

# Display the input data
st.subheader('Patient Input Data')
st.write(input_data)

# Make prediction
if st.button('Predict Diabetes Risk'):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    st.subheader('Prediction')
    diabetes = prediction[0]
    
    if diabetes == 1:
        st.error('High risk of diabetes')
    else:
        st.success('Low risk of diabetes')
    
    st.subheader('Prediction Probability')
    st.write(f'Probability of no diabetes: {prediction_proba[0][0]:.2f}')
    st.write(f'Probability of diabetes: {prediction_proba[0][1]:.2f}')