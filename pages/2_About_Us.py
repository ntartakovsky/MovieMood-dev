import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO
import requests
import json

st.set_page_config(layout="wide")


"""
# About Us

We are a group of grad students at UC Berkeley in the Master of Information and Data Science (MIDS) program. 

MovieMood was founded as part of our capstone class, where we had to develop a data science application, of our choice, from the ground up. 

Our team has a wide/diverse background ranging from data engineering / science to software engineering and UX design. 
"""

st.write(f'<br><br><br>',unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)
cols=[col1,col2,col3,col4,col5]

member_names = ["Neta Tartakovsky", "Sumedh Shah", "Josie Ruggieri", "Neil Prabhu", "Will Dudek"]

for i in range(0,5):    
    with cols[i]:
        st.write(member_names[i])
        st.image('linkedin_img.jpeg', use_column_width="always")