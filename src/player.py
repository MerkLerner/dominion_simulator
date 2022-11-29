from test_cards import *
import random


class Player:
    def __init__(self, _id, game, hand, deck, discard):
        self.id = _id
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
        print(f'player {self.id} action phase')

        actions = []

        for card in self.hand:
            if card.type == "action":
                actions.append(card)

        # what if you draw a new action?
        if len(actions) > 0:
            choice = random.choice(actions)
            print(f'i play {choice}')
            self.play(choice)


    def buy_phase(self):
        print(f'player {self.id} buy phase')

        breakpoint()
        for card in self.hand:
            if card.type == "treasure":
                self.play(card)

        can_buy = []

        all_piles = self.game.piles.all_piles 
        for card_stack in all_piles:
            # remember that there'll be a None
            # one pile depleted
            if (card_stack.size > 0 and
                card_stack.Type.cost <= self.money):
                can_buy.append(card_stack)

        print(f"you have {self.money} money, and can buy {can_buy}")

        if len(can_buy) > 0:
            card = random.choice(can_buy)
            print(f' aw yeah gonna buy {card}')
            self.buy(card)
            self.game.is_game_over() 

    def clean_up(self):
        print(f'player {self.id} clean_up phase')
        # there may be a more performant op here
        self.discard_pile += self.in_play + self.hand
        self.in_play = [] # there also might be a better option to clear it
        self.hand = []
        self.draw(5)
        
        self.money = 0
        self.buys = 1
        self.actions = 1

    def play(self, card, mode="prod"):
        print(f'  playing {card.__class__.__name__}')
        if mode == "prod":
            self.in_play.append(card)
            self.hand.remove(card)

        card.run(self, self.game)
        # think of cards that have 
        # deferred effects

        # also for testing and one offs
        # might not 

    def draw(self, num):
        for _ in range(num):
            # if len(self.deck) == 0: breakpoint()

            if len(self.deck) == 0:   # lets clean up later
                if len(self.discard_pile) == 0:
                    break # if u can't draw no more
                self.shuffle_discard_pile()

            card = self.deck.pop(0)

            # shouldn't do this
            # if card.type == "treasure":
            #     self.money += card.value

            self.hand.append(card)

    def discard(self, card):
        # not guaranteed to be the 
        # same card if there are duplicates
        self.hand.remove(card)

        # careful, make sure we're
        # dealing with piles in uniform ways
        self.discard_pile.append(card)

    def buy(self, card_stack):
        print('i buy now')
        card = card_stack.get_card()
        self.discard_pile.append(card)

    def get_state(self):
        output = f'''Player {self.id}
        actions  buys  money
        {self.actions}        {self.buys}     {self.money}

        cards in hand
        {self.hand}
        '''

        return output

    def shuffle_discard_pile(self):
        print('  reshuffle')
        print(f"      here's the deck {self.deck}")
        print(f"      here's the discard pile {self.discard_pile}")

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
    def has_moat(self):    # really should just flip this when u draw moat
        for card in self.hand:
            if isinstance(card, Moat):
                return True
        return False