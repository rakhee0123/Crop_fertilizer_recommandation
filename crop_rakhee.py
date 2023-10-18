# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:31:40 2023

@author: Rakhee Prajapat
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
#import os

# loading the saved models

#diabetes_model = pickle.load(open('C:/Users/91900/Downloads/diabetes_model.sav', 'rb'))

#heart_disease_model = pickle.load(open('C:/Users/91900/Downloads/heart_disease_model.sav','rb'))


# File paths
Crop_recommandation_model_path = 'C:/Users/91900/Downloads/model.sav'
Crop_yield_model_path = 'C:/Users/91900/Downloads/dtr.sav'
Fertilizer_recommandation_model_path = 'C:/Users/91900/Downloads/classifier1.sav'

# Load models
Crop_recommandation_model = pickle.load(open(Crop_recommandation_model_path, 'rb'))
Crop_yield_model = pickle.load(open(Crop_yield_model_path, 'rb'))
Fertilizer_recommandation_model = pickle.load(open(Fertilizer_recommandation_model_path, 'rb'))
#diabetes_model_path = os.environ.get(diabetes_model_path1)
#heart_disease_model_path = os.environ.get(heart_disease_model_path1)
#os.environ['DIABETES_MODEL_PATH'] = 'C:/Users/91900/Downloads/diabetes_model.sav'
#os.environ['HEART_DISEASE_MODEL_PATH'] = 'C:/Users/91900/Downloads/heart_disease_model.sav'

if Crop_recommandation_model_path is None or Crop_yield_model_path is None or Fertilizer_recommandation_model_path is None:
    st.error("Model paths are not set. Set the environment variables Crop_recommandation_model_path and Crop_yield_model_path and Fertilizer_recommandation_model_path.")
else:
    Crop_recommandation_model = pickle.load(open(Crop_recommandation_model_path, 'rb'))
    Crop_yield_model = pickle.load(open(Crop_yield_model_path, 'rb'))
    Fertilizer_recommandation_model = pickle.load(open(Fertilizer_recommandation_model_path, 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Agriculture System',
                          
                          ['Crop recommandation',
                           
                           'Fertilizer recommandation'],
                          icons=['hand-index','hand-index'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Crop recommandation'):
    
    # page title
    st.title('Crop recommandation using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        N = st.text_input('N')
        
    with col2:
        P = st.text_input('P')
    
    with col3:
        k = st.text_input('K')
    
    with col1:
        temperature = st.text_input('temperature')
    
    with col2:
        humidity = st.text_input('humidity')
    
    with col3:
        ph = st.text_input('ph')
    
    with col1:
        rainfall = st.text_input('rainfall')
    
    
    
    
    # code for Prediction
    Crop_recommand = ''
    
    # creating a button for Prediction
    
    if st.button('Crop Recommandation Result'):
        Crop_recommandation = Crop_recommandation_model.predict([[N,P,k,temperature,humidity,ph,rainfall]])
        
        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

        if Crop_recommandation[0] in crop_dict:
         Crop_recommand = crop_dict[Crop_recommandation[0]]
         Crop_recommand="{} is a best crop to be cultivated ".format(Crop_recommand)
        else:
         Crop_recommand="Sorry are not able to recommend a proper crop for this environment"
        
    st.success(Crop_recommand)

    
if (selected == 'Fertilizer recommandation'):
    
    # page title
    st.title('Fertilizer recommandation using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Nitrogen = st.text_input('Nitrogen')
        
    with col2:
        Potassium = st.text_input('Potassium')
        
    with col3:
        Phosphorous = st.text_input('Phosphorous')
        
   
     
     
    # code for Prediction
    Fertilizer = ''
    
    # creating a button for Prediction
    
    if st.button('Fertilizer recommandation Result'):
        Fertilizer_recommandation = Fertilizer_recommandation_model.predict([[Nitrogen, Potassium, Phosphorous]])                          
        
        if Fertilizer_recommandation[0] == 0:
         Fertilizer= 'TEN-TWENTY SIX-TWENTY SIX'
        elif Fertilizer_recommandation[0] == 1:
         Fertilizer='Fourteen-Thirty Five-Fourteen'
        elif Fertilizer_recommandation[0] == 2:
         Fertilizer='Seventeen-Seventeen-Seventeen' 
        elif Fertilizer_recommandation[0] == 3:
         Fertilizer='TWENTY-TWENTY'
        elif Fertilizer_recommandation[0] == 4:
         Fertilizer='TWENTY EIGHT-TWENTY EIGHT'
        elif Fertilizer_recommandation[0] == 5:
         Fertilizer='DAP'
        else:
         Fertilizer='UREA'
        
    st.success(Fertilizer)
        
    
    


