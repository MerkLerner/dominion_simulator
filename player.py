from test_cards import *
import random

class Player:
    def __init__(self, hand, deck, discard, game):
        self.game = game
        
        self.actions = 1
        self.buys = 1
        self.money = 0

        self.hand = []
        self.in_play = []
        self.discard_pile = []
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
        # there may be a more performant op here
        self.discard_pile += self.in_play + self.hand
        self.in_play = [] # there also might be a better option to clear it
        self.draw(5)
        
        self.money = 0
        self.buys = 1
        self.actions = 1

    def play(self, card, mode="prod"):
        print(f'play {card.__class__.__name__}')
        if mode == "prod":
            self.in_play.append(card)
            self.hand.remove(card)

        card.run(self, self.game)
        # think of cards that have 
        # deferred effects

        # also for testing and one offs
        # might not 

    def draw(self, num):
        print(f'attempting to draw {num} cards')
        for _ in range(num):
            if len(self.deck) == 0: breakpoint()

            if len(self.deck) == 0:   # lets clean up later
                if len(self.discard_pile) == 0:
                    break # if u can't draw no more
                # breakpoint()
                self.shuffle_discard_pile()

            print('  attempting to draw')
            card = self.deck.pop(0)
            print(f'  drew {card}')

            # shouldn't do this
            if card.type == "treasure":
                self.money += card.value

            self.hand.append(card)

    def discard(self, card):
        # not guaranteed to be the 
        # same card if there are duplicates
        self.hand.remove(card)

        # careful, make sure we're
        # dealing with piles in uniform ways
        self.discard_pile.append(card)

    def buy(self, card_stack):
        pass
        # move card from home

    def shuffle_discard_pile(self):
        print('  reshuffle')
        print(f"      here's the deck {self.deck}")
        print(f"      here's the discard pile {self.discard_pile}")

        # breakpoint()
        random.shuffle(self.discard_pile)
        self.deck = self.discard_pile
        self.discard_pile = []
        
        print(f"      here's the deck after: {self.deck}")

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

    @property
    def has_moat(self):
        for card in self.hand:
            if isinstance(card, Moat):
                return True
        return False