from operator import index
import streamlit as st
import plotly.express as px
from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

st.set_page_config(page_title="Build0Brain", page_icon="https://i.ibb.co/CM7vxgY/2.png")

with st.sidebar:
    st.image("https://i.ibb.co/c1wWJxW/image.png",width=300)
sentiment_mapping = ["one", "two", "three", "four", "five"]

st.title("Star Rating")

# Using select slider for star selection
selected = st.select_slider("How many stars would you rate?", 
                            options=range(1, 6),
                            format_func=lambda x: "⭐" * x)

if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected-1]} star(s).")

def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"