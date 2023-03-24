"""
Contains main logic of the app
"""
from src.actions.calendar import CalendarAction
from src.actions.greeting import GreetingAction
from src.actions.weather import WeatherAction
from src.config import Config

if __name__ == '__main__':
    config = Config()
    config.load('config.json')

    greet = GreetingAction(config['personal']['name'])
    weather = WeatherAction(config['weather']['location'][0],
                            config['weather']['location'][1],
                            config['weather']['api_key'],
                            config['weather']['location'][2])
    calendar = CalendarAction()
    
    actions = [greet, weather, calendar]

    for action in actions:
        print(action.call())
        print('')
