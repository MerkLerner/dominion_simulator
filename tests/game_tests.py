'''

    Test file for the `Game` class.

'''
import sys
import unittest

sys.path.append('../')

from src.game import Game

class TestGameSetup(unittest.TestCase):
    def test_number_of_players(self):
        self.game = Game(2)
        self.assertEqual(len(self.game.players), 2)