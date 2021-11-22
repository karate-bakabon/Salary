import streamlit as st
from predict_page import show_predict_page
from predict_page import load_model
from explore_page import show_explore_page
#import numpy as np

page=st.sidebar.selectbox("Explore or predict", ["Predict", "Explore"])

if page=="Predict":
    show_predict_page()
else:
    show_explore_page()





