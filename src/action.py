from abc import ABC, abstractmethod


class Action(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def call(self) -> str:
        raise NotImplementedError("Not implemented")
