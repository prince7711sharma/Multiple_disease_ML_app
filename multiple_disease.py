# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:21:03 2024

@author: CCS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the save data


diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for nacigation
with st.sidebar:st.sidebar.image('data:image/jpeg;base64,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',use_column_width=True)

with st.sidebar:
    
    selected = option_menu('Multiple Disease Pridiction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index = 0)
    # diabetes prediction page
st.image('data:image/jpeg;base64,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',use_column_width=True)    
    
if(selected == 'Diabetes Prediction'):
    
    #page title
    
    st.title('Diabetes Prediction using ML')
    
    # column for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI level')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for pridiction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)
 
if(selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    # column for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain trypes')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Chilestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('FASTING BLOOD sugar >120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Meart Rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('that: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
   
        
    
    # code for pridiction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Heart disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if(heart_prediction[0] == 1):
            heart_diagnosis = 'The person has heart disease'
            
        else:
            heart_diagnosis = 'The person not has heart disease'
            
    st.success(heart_diagnosis)
 
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        #user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
  
 

