import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(page_title="smart Hospital by chacha" , page_icon="🏥", layout="wide")

st.markdown("""
<style>
#MainMenu { visibility: hidden; }
header[data-testid="stHeader"] {display: none;}
.stDeployButton {display: none;}
footer {visibilty; hidden}

</style>
""",unsafe_allow_html=True)

@st.cache_resource
def load_model():
  with open('hospital_model.pkl', 'rb')as f:
    return pickle.load(f)

bundel = load_model()
model = bundel['model']
scaler = bundel['scaler']
feateres = bundel['features']
cols_to_scaler = ['cols_to_scaler']
dep_map_inv = ['dep_map_inv']
gender_map = ['gender_map']
temp_map = ['temp_map']
dur_map = ['dur_map']
cc_map = ['cc_map']

DEPT_INFO = {
    'Respiratory Medicine': {
        'icon':'🫁','color':'#0284c7','bg':'#e0f2fe','border':'#7dd3fc',
        'desc':'Specialises in conditions affecting the lungs and airways.',
        'next':['Visit Level 2, Wing B','Estimated wait: 15–25 min','Please wear a mask']
    },
    'Cardiology': {
        'icon':'❤️','color':'#dc2626','bg':'#fee2e2','border':'#fca5a5',
        'desc':'Specialises in heart and cardiovascular conditions.',
        'next':['Visit Level 3, Wing A','Estimated wait: 20–30 min','Bring any previous ECG reports']
    },
    'Gastroenterology': {
        'icon':'🫃','color':'#d97706','bg':'#fef3c7','border':'#fcd34d',
        'desc':'Specialises in digestive system and abdominal conditions.',
        'next':['Visit Level 1, Wing C','Estimated wait: 10–20 min','Avoid eating before consultation']
    },
    'Neurology': {
        'icon':'🧠','color':'#7c3aed','bg':'#ede9fe','border':'#c4b5fd',
        'desc':'Specialises in brain, spine, and nervous system conditions.',
        'next':['Visit Level 4, Wing A','Estimated wait: 25–35 min','Bring list of current medications']
    },
    'General Medicine': {
        'icon':'🩺','color':'#059669','bg':'#d1fae5','border':'#6ee7b7',
        'desc':'Handles general health concerns and non-specialist conditions.',
        'next':['Visit Level 1, Wing A','Estimated wait: 10–15 min','Registration desk is open 24/7']
    },
    'Dermatology': {
        'icon':'🔬','color':'#b45309','bg':'#fef9c3','border':'#fde68a',
        'desc':'Specialises in skin, hair, and nail conditions.',
        'next':['Visit Level 2, Wing D','Estimated wait: 15–20 min','Bring photos of affected area if possible']
    },
}
st.markdown("""
<div style"pading": 3rem 2rem 2.5rem;margin: -1rem 2rem; tex-align:center;">
<div style="fromt-size:14px; color:white;text-transfrom:uppercase;margin-bottom:12px;>
future classroom : machine learning
<br>
Smart Hospital by Chacha
  </div>
</div>
""",unsafe_allow_html=True)

