# py
import json
from collections import namedtuple
# 3rd party
import requests

WeatherData = namedtuple('WeatherData', 'country city_name weather_main weather_description')

class Country(object):
    def __init__(self, name: str, cities: list):
        self.name = name
        self.cities = cities

    def __iter__(self):
        return iter(self.cities)

    def __len__(self):
        return len(self.cities)

class CountriesWrapper(object):
    endpoint = 'https://countriesnow.space/api/v0.1/countries'

    def get_countries(self):
        json_resp = json.loads(requests.get(self.endpoint).text)
        return [Country(name=country['country'], cities=country['cities']) for country in json_resp['data']]


class WeatherWrapper(object):
    API_KEY = 'a7255c5fb325ba78cda7ed2840888fb1'
    ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

    def get_city_weather(self, city_name: str):
        json_resp = json.loads(requests.get(f"{self.ENDPOINT}?q={city_name}&appid={self.API_KEY}").text)
        return WeatherData(
            country=json_resp['sys']['country'],
            city_name=json_resp['name'],
            weather_main=json_resp['weather'][0]['main'],
            weather_description=json_resp['weather'][0]['description']
        )
