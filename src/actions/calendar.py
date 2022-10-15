"""
Module containing the CalendarAction.
This shows the events in the users Google Calendar
"""

from src.action import Action


class CalendarAction(Action):
    """
    Shows the agenda for today from GCal
    """
    def __init__(self):
        super().__init__('Calendar')

    def call(self) -> str:
        """
        Gets the current time of day and displays a proper greeting to the user
        :return: str, containing the greeeting
        """
        return ''