import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="RAP GPT", page_icon=":microphone:", layout="wide")


st.write("# Welcome to RAP GPT")
st.header("A RNN model to boost rap creativity")

rap_gpt_image = "../images/RAP GPT - Copy.png" 
st.image(rap_gpt_image, use_column_width=True)


st.subheader("Purpose:")
st.markdown("Using the Tensorflow library from Google, to build a generative pre-trained model that was fed with rap lyrics so as to produce a similar output when given a user-specified input.")
st.caption("*Disclaimer*: The model and the analysed data were used _as is_ meaning there was no filter for hard language, just so as to maintain the authenticity of data.")
