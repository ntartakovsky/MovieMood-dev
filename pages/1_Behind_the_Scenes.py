import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        div[data-testid="stStyledFullScreenFrame"] div {
            display: flex;
            justify-content: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

"""
# Behind the Scenes

#### Purpose
Current movie recommendation systems use your movie watching history to make suggestions, but the reality is that the average human listens to music much more frequently than they watch movies. Because of this, movie recommendation engines like Netflix provide a wide variety of recommendations that can be overwhelming and don’t necessarily align with your taste. Finally, several studies have shown how music in films influences the viewer’s experience, outside of non-musical audio and visual information. The crux of MovieMood is to infer someone’s mood and taste from their music playlist and map that to a set of movies that fit the same mood and taste profile. 


#### Data Sources
Spotify's API offers key audio features such as danceability, energy, valence, acousticness, and loudness. We curated playlists representing core moods (happy, sad, energetic, calm) based on psychologist Robert Thayer's model. For our movie dataset, spanning 30+ years, we scraped movies from OMDB and Wikipedia with plot summaries. Finally, to predict likely-to-watch movie genres, we compiled a dataset of 100+ movie soundtracks from Spotify with IMDB genre labels.


#### Implementation 
Using the plot summaries and the genres of each movie, we used Open AI’s GPT 3.5 to produce a sentiment score between 0 and 1 for the four moods (happy, sad, energetic, calm). To predict mood from a music playlist, we used layered classification models to predict the probabilities of those same four moods, as a way to bridge the music and movie worlds. Once this was done, we applied a cosine similarity between the mood profile from the clustered songs to the mood vectors for each movie and got the top movies. Once we got a list of movies matching the mood profile, we then predicted the most probable movie genres a user would watch and applied this as a filter to the movies that were already given, resulting in the top 5 movies you see. 
"""

st.write(f'<br>',unsafe_allow_html=True)
st.image("images/MovieMood_Arch.png")
st.write(f'<br><br>',unsafe_allow_html=True)

"""

#### Acknowledgements
We wanted to thank our instructors, Joyce Shen and Todd Holloway, for their guidance and ongoing support for this project. We then wanted to thank fellow classmate, Max Eagle, for providing us with our data source and data gathering technique for all of the movies we used in the project. Finally, we want to thank Chris Volinsky, NYU Professor/Netflix Prize winner who used to work at AT&T’s Chief Data Office with Sumedh, for his guidance and insightful comments on our modeling approach for MovieMood.

"""