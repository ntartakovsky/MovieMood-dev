import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO
import requests
import json

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def get_data(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("successfully fetched the data")
        print(response.json())
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")
    return response.json()



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    url = "https://neilprabhu.mids255.com/predict"
 
    headers = {"Content-Type": "application/json"}

    arr = df.to_numpy()

    data = {
        "music_list":[["Danceability","Energy","Key","Loudness","Mode","Speechiness","Acousticness","Instrumentalness","Liveness","Valence","Tempo","Time Signature"]]
    }

    for item in arr:
        list_str = list(item)[-12:]
        new_list = []
        for num in list_str:
            new_list.append(str(num))
        data['music_list'].append(new_list)

    recs = get_data(url, headers, data)

    st.write(recs)


















