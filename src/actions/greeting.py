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

    def call(self) -> str:
        """
        Gets the current time of day and displays a proper greeting to the user
        :return: str, containing the greeeting
        """
        now = datetime.now()

        current_hour = int(now.strftime('%H'))

        if 6 <= current_hour <= 11:
            part_of_day = 'Good morning'
        elif 12 <= current_hour <= 14:
            part_of_day = 'Hello'
        elif 15 <= current_hour <= 18:
            part_of_day = 'Good afternoon'
        else:
            part_of_day = 'Good evening'

        greeting = "{part_of_day}, {name}. Today is {current_date}. The time is {current_time}."
        current_date = now.strftime("%A, %d %B %Y")
        current_time = now.strftime("%H:%M")

        return greeting.format(part_of_day=part_of_day, name=self.__name,
                               current_date=current_date, current_time=current_time)
