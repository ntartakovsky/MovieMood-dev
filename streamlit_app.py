import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO
import requests
import json

"""
# Welcome to MovieMood!

Upload your Spotify playlist in a csv file below:
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


    col1,col2,col3,col4,col5=st.columns(5)
    cols=[col1,col2,col3,col4,col5]
    for i in range(0,5):
        with cols[i]:
            title = recs['movies_list'][i]['omdb_title']
            poster = recs['movies_list'][i]['omdb_poster']
            st.write(f' <b style="color:#E50914"> {title} </b>',unsafe_allow_html=True)
            # st.write("#")
            st.image(poster)

















