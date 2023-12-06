import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64
st.set_page_config(page_title="RAP GPT", page_icon=":microphone:", layout="wide")

st.header("The data collection process")

# 1 and 2 denote that column 1 (where I put my rap_genius img) is 1/3 of the width and col2 is 2/3
col1, col2 = st.columns([1, 4])

# image to the first column
genius_logo = "../images/Rap_genius.png"
col1.image(genius_logo, caption="https://genius.com/", width=150)

# text to the second column
col2.write("Genius is arguably the most popular website to check lyrics from. They've gained popularity due to the interaction model they've built around the lyrics where users can contribute with 'anotations' to explain the meaning of lyrics they might be aware of.")
col2.write("They've developed an API on top of which the *'lyricsgenius'* library was built scrapping information from it using beautifulSoup. For this project I've used this library.")

st.subheader("A total of 13,305 lyrics were fetched from the website:")

# Inserting a gif:
fetching_lyrics_gif = open("../images/GIF fetching lyrics.gif", "rb")
contents = fetching_lyrics_gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
fetching_lyrics_gif.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="fetching lyrics" width="1030">',
    unsafe_allow_html=True,
)

# text again:
st.markdown("A function fetches the lyrics sleeping for 1sec between each fetch and taking a deeper breath after 60 fetches. This was mainly to avoid overrequesting and being able to run the code for long periods of time.")
st.markdown("Another function compiles all the .txt into one file for each artist to be able to generate statistics individually per artist and yet another one compiled every lyric into one file only:")

# Inserting another gif, the compilation one:
compiling_artists_gif = open("../images/GIF Compiling artists.gif", "rb")
contents = compiling_artists_gif.read()
data_url = base64.b64encode(contents).decode("utf-8")
compiling_artists_gif.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="compiling compiling artists" width="1030">',
    unsafe_allow_html=True,
)

st.subheader("The total compilation file retrieved more than 35M characters. For reference, Romeo&Juliet is around 1M total.")
st.markdown("However, more information does not necessarily equate to a better model, if anything it hindered the model as many artists have too many different styles. Also: processing time.")

st.caption("*(...) it sounds strange but the rap game is not a game / you could make a lotta money, gain a lotta fame / But don't get it twisted, you could get addicted / buy a mansion in the Hamptons, and get evicted (...)*")