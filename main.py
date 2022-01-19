import streamlit as st
from models import generate_map
import os
from dotenv import find_dotenv, load_dotenv

env_loc = find_dotenv('.env')
load_dotenv(env_loc)

map_fig = generate_map()

## Streamlit App
# Header Text
st.title("**Geocoder2**")
st.plotly_chart(map_fig)