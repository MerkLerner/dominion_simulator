from test_cards import Copper, Estate
import random

class Player:
    def __init__(self, hand, deck, discard):
        self.actions = 1
        self.buys = 1
        self.money = 0

        self.hand = []
        self.discard = []
        self.deck = self.init_deck()
        self.draw(5)

        # careful here. we'll want to 
        # set specific conditions later
        
        self.victory_points = 3
        # sorta nice to track
        # necessary for AI
        # but if no AI,
        # only needed at end game

    def play(self, card):
        card.run(self)

    def draw(self, num):
        # think about deck running out
        if len(self.deck) == 0:
            print('hoopa')

        # essentially - 
        # if deck empty
        #    shuffle discard
        #    deck = discard
        #    discard clear
        # if discard empty
        #    fizzle
        # otherwise, 
        #   draw

        for _ in range(num):
            card = self.deck.pop(0)
            
            if card.type == "money":
                self.money += card.value

            self.hand.append(card)

    def discard(self):
        pass

    def init_deck(self):
        deck = [
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper()
            Estate(),
            Estate(),
            Estate()
        ]

        random.shuffle(deck)

        return deck

    # move card

    # buy