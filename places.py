class Piles:
    def __init__(self,):
        self.v_cards = []
        self.money_cards = []
        self.curses = []

        self.kingdom_cards = []

        self.all_piles = self.v_cards \
            + self.money_cards \
            + self.curses \
            + self.kingdom_cards


class Trash:
    def __init__(self):
        self.can = [] # should this be an empty stack?
