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
