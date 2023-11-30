import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO
import requests
import json

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        div[data-testid="stLinkButton"] p
        {
            font-size: 0.8rem !important;
        } 

        div[role=radiogroup] label:first-of-type 
        {
            visibility: hidden;
            height: 0px;
            width: 0px;
        }

        div[data-testid="stLinkButton"]
        {
            text-align: center;
        }

        .stRadio [role=radiogroup]
        {
            align-items: center;
            justify-content: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def get_data(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("successfully fetched the data")
        print(response.json())
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")
    return response.json()


# Set up the title & introduction!
"""
# Welcome to MovieMood!

We use your Spotify playlist to recommend movies that match your mood.
"""

"""
#
To use our engine, you will need to upload a CSV file containing your Spotify playlist details.
Instructions to retrieve your CSV file:
1. Navigate to www.exportify.net. 
2. Log in with your Spotify credentials.
3. Select and download the playlist that you would like to use.
"""

# Define the file uploader and filters
uploaded_file = st.file_uploader("Upload your Spotify playlist CSV file below:")

filter_genres = []
filter_ratings = []
with st.expander("See optional filters for movie recommendations"):
    filter_genres = st.multiselect(
        'What are your preferred movie genres?',
        ['Comedy', 'Horror', 'Drama', 'Romance'])

    filter_ratings = st.multiselect(
        'What are your preferred movie ratings?',
        ['G', 'PG', 'PG-13', 'R', 'Unrated'])


# Get the movie recommendations and display them
if uploaded_file is not None:

    # Pull the spotify CSV file and reformat the music data for the API call
    df = pd.read_csv(uploaded_file)
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

    # Add the filter selections to the data for the API call
    data["filter_ratings"] = list(filter_ratings)
    data["filter_genres"] = [x.lower() for x in list(filter_genres)]

    # Define remaining API parameters
    url = "https://neilprabhu.mids255.com/predict"
    headers = {"Content-Type": "application/json"}

    # Call the API to get the movie recs
    recs = get_data(url, headers, data)



    # Set up the button to regenerate the recommendations
    if st.button("Regenerate Recommendations", key="get_recs"):
        # "drop_movies": [{"omdb_title":"Luca","omdb_director":"Enrico Casarosa"},{"omdb_title":"Kiss of the Dragon","omdb_director":"Chris Nahon"}]
        recs = get_data(url, headers, data)

        



    # Display the movie recommendations & details

    col1,col2,col3,col4,col5=st.columns(5)
    cols=[col1,col2,col3,col4,col5]
    
    for i in range(0,5):
        with cols[i]:
            title = recs['movies_list'][i]['omdb_title']
            poster = recs['movies_list'][i]['omdb_poster']
            plot = recs['movies_list'][i]['omdb_plot']
            genres = recs['movies_list'][i]['genres']
            director = recs['movies_list'][i]['omdb_director']
            actors = recs['movies_list'][i]['omdb_actors']
            imdb_score = recs['movies_list'][i]['imdb_score']
            runtime = recs['movies_list'][i]['omdb_runtime']
            rated = recs['movies_list'][i]['rated']
            imdb_url = recs['movies_list'][i]['imdb_url']

            st.write(f' <p style="font-size: 0.9rem;height: 50px;display: flex;align-items: end;font-weight: 600;"> {title} </p>',unsafe_allow_html=True)
            st.image(poster, use_column_width="always")
            
            movie_string = "movie_" + str(i+1)

            review = st.radio(label="", 
                             options=["hidden", ":thumbsup:", ":thumbsdown:"], 
                             key=title+"-"+director+"-review",
                             horizontal=True,
                             label_visibility="collapsed")
            

            with st.expander("More details"):
                st.write(f' <p style="font-size:0.75rem"> {plot} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> Runtime: {runtime} minutes</p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> Rated: {rated} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> IMDB Score: {imdb_score} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> Genres: {genres} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> Directed by: {director} </p>',unsafe_allow_html=True)
                st.write(f' <p style="font-size:0.75rem"> Leading Actors: {actors} </p>',unsafe_allow_html=True)
                st.link_button("Go to IMDB Page →", imdb_url)















