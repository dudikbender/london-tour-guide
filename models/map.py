import pandas as pd
from pandas import json_normalize
import plotly.express as px
import plotly.graph_objects as go
from os import environ
from dotenv import load_dotenv
from .load_data import retrieve_data

load_dotenv()
mapbox_token = environ.get('MAPBOX_TOKEN')
px.set_mapbox_access_token(mapbox_token)

def generate_map(style: str):
    df = pd.DataFrame(retrieve_data()['Sites']).reset_index(drop=True).transpose().reset_index()
    df.columns = ['Name','Address','Category','Description','importance','lat','lon']
    df['importance'] = [ int(x) for x in df.importance ]
    fig = px.scatter_mapbox(df, 
                            lat='lat', 
                            lon='lon',
                            color='Category',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            center={'lat':51.5, 'lon':-0.15},
                            zoom=12,
                            size='importance',
                            size_max=30,
                            hover_data={'Name':True,
                                        'Category':True,
                                        'Description':True,
                                        'importance':True,
                                        'Address':True,
                                        'lat':False,
                                        'lon':False,
                                        },
                            mapbox_style=style,
                            width=700,
                            height=650
                            )
    return fig