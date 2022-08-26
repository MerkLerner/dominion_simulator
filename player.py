from test_cards import Copper, Estate
import random

class Player:
    def __init__(self, hand, deck, discard, game):
        self.game = game
        
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
    
    def action_phase(self):
        actions = []

        for card in self.hand:
            if card.type == "action":
                actions.append(card)

        if len(actions) > 0:
            choice = random.choice(actions)
            print(f'i play {choice}')
            self.play(card)

    def buy_phase(self):
        can_buy = []

        all_piles = self.game.piles.all_piles 
        for card_stack in all_piles:
            # remember that there'll be a None
            # one pile depleted
            if card_stack.Type.cost <= self.money:
                can_buy.append(card_stack)

        print(self.money, can_buy, len(self.hand))

    def clean_up(self):
        print('clean up')

    def play(self, card, game):
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
            
            if card.type == "treasure":
                self.money += card.value

            self.hand.append(card)

    def discard(self, card):
        # not guaranteed to be the 
        # same card if there are duplicates
        temp = self.hand.remove(card)

        # careful, make sure we're
        # dealing with piles in uniform ways
        self.discard.append(temp)

    def init_deck(self):
        deck = [
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Copper(),
            Estate(),
            Estate(),
            Estate()
        ]

        random.shuffle(deck)

        return deck

    # move card

    def buy(self, card_stack):
        pass
        # move card from home