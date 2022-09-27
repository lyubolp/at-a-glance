import os
import json


class Config:
    def __init__(self):
        self.__items = {}

    def load(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f'File {path} does not exist')

        with open(path) as fp:
            try:
                content = json.load(fp)
            except json.JSONDecodeError as ex:
                raise ex

            self.__items = content

    def __getitem__(self, item) -> any:
        return self.__items[item]

