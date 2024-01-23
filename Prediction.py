import numpy as np 
import pickle
import streamlit as st
import os

# Loading the ML model Using pickle
loaded_model = pickle.load(open('E:/Downloads/sav file/heart_disease_trained.sav', 'rb'))

# Creating a function for Prediction
def heart_disease_prediction(input_data):
    # Converting the input data as numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshaping the numpy array because we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Now predicting for our input data
    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)


    if prediction [0] == 1:
            return 'The Person has Heart Disease'
    else:
            return 'The Person doesnt have heart disease'
    

def main():
    # Giving a Title for the Web App
    st.title("Heart Disease Prediction Web Application")

    # Getting input data from the user for Prediction
    age = st.text_input('Age of the Person')
    sex = st.text_input('Sex of the Person')
    cp = st.text_input('CP value')
    trestbps = st.text_input('Trestbps value')
    chol = st.text_input('Chol value')
    fbs = st.text_input('FBS value')
    restecg = st.text_input('Restecg value')
    thalach = st.text_input('Thalach value')
    exang = st.text_input('Exang value')
    oldpeak = st.text_input('Oldpeak value')
    slope = st.text_input('Slope value')
    ca = st.text_input('CA value')
    thal = st.text_input('Thal value')

    # Convert input values to integers
    age = int(age) if age.isdigit() else 0
    sex = int(sex) if sex.isdigit() else 0
    cp = int(cp) if cp.isdigit() else 0
    trestbps = int(trestbps) if trestbps.isdigit() else 0
    chol = int(chol) if chol.isdigit() else 0
    fbs = int(fbs) if fbs.isdigit() else 0
    restecg = int(restecg) if restecg.isdigit() else 0
    thalach = int(thalach) if thalach.isdigit() else 0
    exang = int(exang) if exang.isdigit() else 0
    oldpeak = int(oldpeak) if oldpeak.isdigit() else 0
    slope = int(slope) if slope.isdigit() else 0
    ca = int(ca) if ca.isdigit() else 0
    thal = int(thal) if thal.isdigit() else 0
    
    # Code for prediction
    diagnosis = ''

    # Creating a Button for Prediction
    if st.button('Heart Diseases Test Result'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        

    st.success(diagnosis)

if __name__ =='__main__':
   main()
