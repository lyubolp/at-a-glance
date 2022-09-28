import requests
import sys
import json

from action import Action
from datetime import datetime


class WeatherAction(Action):
    def __init__(self, lat: float, lon: float, api_key: str, city_name: str):
        super(WeatherAction, self).__init__('Weather')

        self.__lat = lat
        self.__lon = lon
        self.__api_key = api_key
        self.__city_name = city_name

    def call(self) -> str:
        weather_now = self.__get_weather_now()
        weather_today = self.__get_weather_today()
        return weather_now + '\n' + weather_today

    def __get_weather_now(self) -> str:
        weather_now = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
        response = self.__get_weather_from_api(weather_now)

        weather_like = response['weather'][0]['main']
        temperature = response['main']['temp']
        result = 'The weather in ' + self.__city_name + ' is ' + weather_like + \
                 '. The temperature now is ' + str(int(temperature)) + '°'

        return result

    def __get_weather_today(self) -> str:
        weather_today = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric'

        response = self.__get_weather_from_api(weather_today)

        weather = response['list']
        current_day = datetime.now().strftime('%Y-%m-%d')
        temp_today = [WeatherAction.__get_weather_text_for_today(item) for item in weather if current_day in item['dt_txt']]

        result = 'The weather in ' + self.__city_name + ' today will be ' + '. '.join(temp_today)

        return result

    @staticmethod
    def __get_weather_text_for_today(weather_hour: dict) -> str:
        weather_temp = str(int(weather_hour['main']['temp']))
        weather_type = weather_hour['weather'][0]['main']
        weather_hour = weather_hour['dt_txt'].split(' ')[1]
        return weather_temp + '°, ' + weather_type + ', at ' + weather_hour

    def __get_weather_from_api(self, request_url: str):
        request_url = request_url.format(lat=self.__lat, lon=self.__lon, api_key=self.__api_key)

        # print(request_url)

        resp = requests.get(url=request_url)
        if resp.status_code != 200:
            return 'Invalid api key or city name'

        return resp.json()
