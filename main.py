import streamlit as st
import pandas as pd
from models import generate_map, retrieve_data
import os
from dotenv import find_dotenv, load_dotenv

env_loc = find_dotenv('.env')
load_dotenv(env_loc)



## Streamlit App
# Header Text
st.title("Our Tour of London")

df = pd.DataFrame(retrieve_data()['Sites']).reset_index(drop=True).transpose().reset_index()
df.columns = ['Name','Address','Category','Description','importance','lat','lon']
df = df[['Name','Category','Description','importance']].sort_values('importance', ascending=False)
#df['importance'] = [ int(x) for x in df.importance ]
st.dataframe(df)

style_options = ['open-street-map', 'white-bg', 'carto-positron', 'carto-darkmatter', 'stamen- terrain', 
                 'stamen-toner', 'stamen-watercolor','basic', 'streets', 'outdoors', 'light', 'dark', 
                 'satellite', 'satellite- streets']

style_select = st.selectbox(label='Select map style', options=style_options, index=5)
map_fig = generate_map(style=style_select)

st.plotly_chart(map_fig)