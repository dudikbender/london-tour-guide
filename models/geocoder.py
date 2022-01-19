import json
import requests
import os
from dotenv import find_dotenv, load_dotenv
env_loc = find_dotenv()
load_dotenv(env_loc)

class Geocoder():
    def __init__(self, address: str):
        self.api_key = os.environ.get('GOOGLE_TOKEN')
        self.address = address

    def _geocode(self):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'address':self.address,'key':self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def return_lat_lng(self):
        response = self._geocode()
        try:
            location = response['results'][0].get('geometry',{}).get('location')
            lat, lng = location.get('lat'), location.get('lng')
            return lat, lng
        except Exception as e:
            print(response)
            return