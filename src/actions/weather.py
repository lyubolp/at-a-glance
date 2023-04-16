"""
Contains the Weather action, which returns the weather now,
as well as the weather until the end of the day
"""
from datetime import datetime

import requests

from src.action import Action


class WeatherAction(Action):
    """
    Implements requests to OpenWeatherMap API to get info about the weather.
    """

    def __init__(self, lat: float, lon: float, api_key: str, city_name: str):
        """
        For the API to work, we need an API key,
            as well as the coordinates of the location for which we will show the weather.
        :param lat: latitude of the location
        :param lon: longitude of the location
        :param api_key: API key for OpenWeatherMap
        :param city_name: The name of the location
        """
        super().__init__('Weather')

        self.__lat = lat
        self.__lon = lon
        self.__api_key = api_key
        self.__city_name = city_name

        self.__main_url = 'https://api.openweathermap.org/data/2.5/weather?'

    def call(self) -> str:
        """
        Returns the weather now and the weather for today
        :return:
        """
        weather_now = self.__get_weather_now()
        weather_today = self.__get_weather_today()
        return weather_now + '\n' + weather_today

    def __get_weather_now(self) -> str:
        """
        Returns the weather and temperature for a given location
        :return: str, containing the action result
        """
        weather_now = self.__main_url + 'lat={lat}&lon={lon}&appid={api_key}&units=metric'
        response = self.__get_weather_from_api(weather_now)

        weather_like = response['weather'][0]['main']
        temperature = response['main']['temp']
        result = 'The weather in ' + self.__city_name + ' is ' + weather_like + \
                 '. The temperature now is ' + str(int(temperature)) + '°'

        return result

    def __get_weather_today(self) -> str:
        """
        Returns the weather and temperature for a given location until the end of the day
        :return: str, containing the action result
        """
        weather_today = 'https://api.openweathermap.org/data/2.5/forecast?' + \
            'lat={lat}&lon={lon}&appid={api_key}&units=metric'

        response = self.__get_weather_from_api(weather_today)

        weather = response['list']
        current_day = datetime.now().strftime('%Y-%m-%d')
        temp_today = [WeatherAction.__get_weather_text_for_today(item)
                      for item in weather if current_day in item['dt_txt']]

        result = 'The weather in ' + self.__city_name + ' today will be ' + '. '.join(temp_today)

        return result

    @staticmethod
    def __get_weather_text_for_today(weather_hour: dict) -> str:
        """
        Returns a human-readable info for the weather at a given time
        :param weather_hour: the response for the current hour
        :return: Returns a string containing the temp and weather at the given hour
        """
        weather_temp = str(int(weather_hour['main']['temp']))
        weather_type = weather_hour['weather'][0]['main']
        weather_hour = weather_hour['dt_txt'].split(' ')[1]
        return weather_temp + '°, ' + weather_type + ', at ' + weather_hour

    def __get_weather_from_api(self, request_url: str):
        """
        Sends a request to a given URL
        :param request_url: The URL to send the request to
        :return: The JSON request response
        """
        request_url = request_url.format(lat=self.__lat, lon=self.__lon, api_key=self.__api_key)

        # print(request_url)

        # TODO: Handle timeout
        resp = requests.get(url=request_url, timeout=10)
        if resp.status_code != 200:
            return 'Invalid api key or city name'

        return resp.json()
