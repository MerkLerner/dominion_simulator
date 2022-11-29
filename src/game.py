from places import Piles
from player import Player


class Game:
    def __init__(self, player_count=1):
        self.piles = Piles()

        players = []
        for _id in range(player_count):
            players.append(Player(_id+1, self, [], [], []))

        self.players = set(players)

    def is_game_over(self):
        # breakpoint()
        if (self.piles.v_cards[2] == 0 or          #ugh fix. provinces
          len(self.piles.all_piles) <= 14):        # shouldn't there be 10 kingdom pile?
            # assuming this includes curses
            # also, gotta change so we can 
            # do the all card game
            # gameOver = True
            raise Exception('Game over')

    def add_up_points(self):
        # oooh i could use thread to total up
        # the different players 

        # actually that's really interesting.
        # threaded version of this app could 
        # treat each player as completely siloed
        # and just send messages to other thread
        # about events in one that could force the 
        # other to recalculate. whether that 
        # results in a performance gain is tricky 
        # tho. in a game with no attack cards,
        # folx just need to know about when a pile
        # is gone or when game is over...
        # eeeeh that's tricky though...

        # okay. i think i may nix that. that might be a 
        # loooooooot of recalculating depening on the lag

        # interesting. players are not quite but sort
        # of equivalent
        pass