from test_cards import *


class Stack:
    def __init__(self, CardType, size):
        self.Type = CardType()
        self._stack = []

        for _ in range(size):
            self._stack.append(CardType())

    def get_card(self):
        if self.size <= 0:
            raise Exception('hey, i"m empty!')

        return self._stack.pop(-1)

    def __repr__(self):
        s = f"{self.Type.__class__.__name__} ({self.size})"
        return s

    @property  # should maybe just use __len__, faster
    def size(self):
        return len(self._stack)

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
            Stack(Copper, 60),
            Stack(Silver, 40),
            Stack(Gold, 30)
        ]

        self.curses = [
            Stack(Curse, 10)
        ]

        # I'll want to be able to 
        # instantiate these directly 
        # as well
        self.kingdom_cards = [
            Stack(Cellar, 10),
            Stack(CouncilRoom, 10),
            Stack(Festival, 10),
            Stack(Laboratory, 10),
            Stack(Market, 10),
            Stack(Militia, 10),
            Stack(Moat, 10),
            Stack(Poacher, 10),
            Stack(Smithy, 10),
            Stack(Village, 10),
        ]

        self.all_piles = self.v_cards \
            + self.money_cards \
            + self.curses \
            + self.kingdom_cards

class Trash:
    def __init__(self):
        self.can = [] # should this be an empty stack?