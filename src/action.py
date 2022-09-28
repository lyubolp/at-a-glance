"""
Contains the Abstract Action class, from which all actions
"""
from abc import ABC, abstractmethod


class Action(ABC):
    """
    The abstract base class for the Actions.
    All actions must inherit from this class
    """
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        """
        Returns the name of the action
        :return: str, containing the name of the action
        """
        return self.__name

    @abstractmethod
    def call(self) -> str:
        """
        Main method that is called. Executes the action and returns the human-readable output
        :return: str, containing the output of the action
        """
        raise NotImplementedError("Not implemented")
