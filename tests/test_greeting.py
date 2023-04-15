import unittest

from datetime import datetime
from unittest.mock import patch

from src.actions.greeting import GreetingAction


class TestGreetingAction(unittest.TestCase):
    """
    Tests the GreetingAction
    """
    def test_01_greeting(self):
        """
        Tests the greeting action
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_02_morning_1(self, mock_datetime):
        """
        Tests the greeting action in the morning
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 6, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good morning'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_03_morning_2(self, mock_datetime):
        """
        Tests the greeting action in the morning
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 11, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good morning'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_04_morning_3(self, mock_datetime):
        """
        Tests the greeting action in the morning
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 8, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good morning'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_05_hello_1(self, mock_datetime):
        """
        Tests the greeting action around lunch time
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 12, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Hello'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_06_hello_2(self, mock_datetime):
        """
        Tests the greeting action around lunch time
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 14, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Hello'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_07_hello_3(self, mock_datetime):
        """
        Tests the greeting action around lunch time
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 12, 53, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Hello'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_08_afternoon_1(self, mock_datetime):
        """
        Tests the greeting action in the afternoon
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 15, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good afternoon'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_09_afternoon_2(self, mock_datetime):
        """
        Tests the greeting action in the afternoon
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 18, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good afternoon'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_10_afternoon_3(self, mock_datetime):
        """
        Tests the greeting action in the afternoon
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 17, 21, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good afternoon'))
        self.assertTrue(name in result)

    @patch('src.actions.greeting.datetime')
    def test_11_evening_1(self, mock_datetime):
        """
        Tests the greeting action in the evening
        :return: None
        """
        # Arrange
        name = 'John'
        action = GreetingAction(name)

        # Act
        with patch('src.actions.greeting.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 4, 11, 19, 1, 0)
            result = action.call()

        # Assert
        self.assertTrue(result.startswith('Good evening'))
        self.assertTrue(name in result)
