import requests
import sys
import json

from action import Action


class WeatherAction(Action):
    def __init__(self, lat: float, lon: float, api_key: str, city_name: str):
        super(WeatherAction, self).__init__('Weather')

        self.__lat = lat
        self.__lon = lon
        self.__api_key = api_key
        self.__city_name = city_name

    def call(self) -> str:
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
        url = url.format(lat=self.__lat, lon=self.__lon, api_key=self.__api_key)

        resp = requests.get(url=url)
        if resp.status_code != 200:
            return 'Invalid api key or city name'

        weather_like = resp.json()['weather'][0]['main']
        temperature = resp.json()['main']['temp']
        result = 'The weather in ' + self.__city_name + ' is ' + weather_like + \
                 '. The temperature is ' + str(temperature) + ' degrees celsius'

        return result
