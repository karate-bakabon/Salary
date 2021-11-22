import streamlit as st
import pickle
import numpy as np
#import pandas as pd

def load_model():
    file_name = 'saved_steps.pkl'
    with open(file_name, 'rb') as f:
        model = pickle.load(f)
    return model

data=load_model()
regressor=data['model']
le_country=data['le_country']
le_education=data['le_education']

def show_predict_page():
    st.title('Software Developer Predict Salary')
    st.write("""### We need some information to predict the salary""")
    
    countries=(
        "United States", 
        "India",                 
        "United Kingdom",        
        "Germany",               
        "Canada",                
        "Brazil",                 
        "France",                 
        "Spain",                  
        "Australia",              
        "Netherlands",            
        "Poland",                 
        "Italy",                  
        "Russian Federation",     
        "Sweden",          
      )

    education=(
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Post grad',
        'Master’s degree',
    )

    country=st.selectbox("Country",countries)
    education=st.selectbox("Education",education)

    experience=st.slider("Years of experience",0,50,3)

    ok=st.button("Calculate Salary:")


    if ok:
        x=np.array([[country,education,experience]])
        x[:,0]=le_country.transform(x[:,0])
        x[:,1]=le_education.transform(x[:,1])
        x=x.astype(float)

        salary=regressor.predict(x)
        st.subheader(f"The estimate salary is ${salary[0]:.2f}")


#show_predict_page()