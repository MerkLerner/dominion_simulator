from test_cards import *


class Stack:
    def __init__(self, CardType, size):
        self.Type = CardType()
        self._stack = []

        for _ in range(size):
            self._stack.append(CardType())

        self._len = size


class Piles:
    def __init__(self,):
        # come back here later
        # stack size dependent on
        # number of players
        self.v_cards = [
            Stack(Estate, 8),
            Stack(Duchy, 8),
            Stack(Province, 8)
        ]

        self.money_cards = [
            Stack(Copper, 8),
            Stack(Silver, 8),
            Stack(Gold, 8)
        ]

        self.curses = [
            Stack(Curse, 30)
        ]

        # I'll want to be able to 
        # instantiate these directly 
        # as well
        self.kingdom_cards = []

        self.all_piles = self.v_cards \
            + self.money_cards \
            + self.curses \
            + self.kingdom_cards


class Trash:
    def __init__(self):
        self.can = [] # should this be an empty stack?