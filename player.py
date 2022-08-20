class Player:
    def __init__(self, hand, deck, discard):
        self.hand = []
        self.deck = []
        self.discard = []

        self.actions = 1
        self.buys = 1
        self.money = 0
        
        self.victory_points = 3

    def play(self, card):
        card.run(self)

    def draw(self, num):
        # think about deck running out
        if len(self.deck) == 0:
            print('hoopa')

    def discard(self):
        pass

    # move card

    # buy