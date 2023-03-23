"""
Contains the classes responsible for reading from config files
"""
import os
import json

from typing import Any


class Config:
    """
    Reads from the main config.json file
    """
    def __init__(self):
        self.__items = {}

    def load(self, path: str):
        """
        Loads the JSON config file. Keeps the items in-memory.
        :param path: The path to the file to read from
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f'File {path} does not exist')

        with open(path, encoding='UTF-8') as file_pointer:
            try:
                content = json.load(file_pointer)
            except json.JSONDecodeError as ex:
                raise ex

            self.__items = content

    def __getitem__(self, item) -> Any:
        return self.__items[item]
