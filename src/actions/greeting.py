"""
Module containing the GreetingAction.
This greets the user, by showing the time of day.
"""
from datetime import datetime
from src.action import Action


class GreetingAction(Action):
    """
    Greets the user
    """

    def __init__(self, name: str):
        super().__init__('Greeting')

        self.__name = name
        self.__greeting = '{part_of_day}, {name}. ' + \
            'Today is {current_date}. ' + \
            'The time is {current_time}.'

    def call(self) -> str:
        """
        Gets the current time of day and displays a proper greeting to the user
        :return: str, containing the greeeting
        """
        now = datetime.now()

        current_hour = int(now.strftime('%H'))

        part_of_day = self.__generate_part_of_day(current_hour)
        current_date = now.strftime("%A, %d %B %Y")
        current_time = now.strftime("%H:%M")

        return self.__greeting.format(part_of_day=part_of_day, name=self.__name,
                                      current_date=current_date, current_time=current_time)

    @staticmethod
    def __generate_part_of_day(current_hour: int) -> str:
        """
        Gets the current hour and returns the part of the day
        :param current_hour: int, the current hour
        :return: str, the part of the day
        """
        if 6 <= current_hour <= 11:
            return 'Good morning'
        if 12 <= current_hour <= 14:
            return 'Hello'
        if 15 <= current_hour <= 18:
            return 'Good afternoon'

        return 'Good evening'
