# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_human_tic_tac_toe_agent

import unittest
import time
from human_tic_tac_toe_agent import HumanTicTacToeAgent


class TestHumanTicTacToeAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A HumanTicTacToeAgent exists.
        """
        try:
            HumanTicTacToeAgent(None, None)
        except NameError:
            self.fail("Could not instantiate HumanTicTacToeAgent")

    """
    Properties
    """

  