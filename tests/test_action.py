"""
Contains the Action class unit tests
"""
import unittest

from src.action import Action


class TestAction(unittest.TestCase):
    """
    Test the Action class
    """
    def test_01_name(self):
        """
        Tests if the name is set correctly
        """

        class ActionInternal(Action):
            """
            Action for testing
            """
            def call(self) -> str:
                return "test"

        name = "test"
        action = ActionInternal(name)
        self.assertEqual(action.name, name)

    def test_02_call(self):
        """
        Tests if the call method is implemented
        """

        class ActionInternal(Action):
            """
            Action for testing
            """
            def call(self) -> str:
                return "test"

        action = ActionInternal("test")
        self.assertEqual(action.call(), "test")
