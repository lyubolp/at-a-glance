import json
import os
import unittest

from src.config import Config


class TestConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Creates a temporary JSON file
        """
        cls.__temp_json_file_path = 'temp.json'
        TestConfig.__create_temp_json_file(cls.__temp_json_file_path)
    
    @classmethod
    def tearDownClass(cls):
        """
        Deletes the temporary JSON file
        """
        TestConfig.__delete_temp_json_file(cls.__temp_json_file_path)

    @staticmethod
    def __create_temp_json_file(filename: str):
        """
        Creates a temporary JSON file
        """
        with open(filename, 'w+', encoding='utf-8') as file_pointer:
            json.dump({"name": "test"}, file_pointer)

    @staticmethod
    def __delete_temp_json_file(filename: str):
        """
        Deletes the temporary JSON file
        """
        os.remove(filename)

    def test_01_load(self):
        """
        Tests if the config file is loaded correctly
        """

        # Arrange
        config = Config()

        # Act
        config.load("config.json")

        # Assert
        self.assertEqual(config["name"], "test")
