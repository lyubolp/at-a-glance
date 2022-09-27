from actions.weather import WeatherAction
from config import Config

if __name__ == '__main__':
    config = Config()
    config.load('config.json')

    weather = WeatherAction(config['weather']['location'][0],
                            config['weather']['location'][1],
                            config['weather']['api_key'],
                            config['weather']['location'][2])

    actions = [weather]

    for action in actions:
        print(action.call())
