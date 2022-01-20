import streamlit as st
from models import generate_map
import os
from dotenv import find_dotenv, load_dotenv

env_loc = find_dotenv('.env')
load_dotenv(env_loc)



## Streamlit App
# Header Text
st.title("Our Tour of London")

style_options = ['open-street-map', 'white-bg', 'carto-positron', 'carto-darkmatter', 'stamen- terrain', 
                 'stamen-toner', 'stamen-watercolor','basic', 'streets', 'outdoors', 'light', 'dark', 
                 'satellite', 'satellite- streets']

style_select = st.selectbox(label='Select map style', options=style_options, index=0)
map_fig = generate_map(style=style_select)

st.plotly_chart(map_fig)