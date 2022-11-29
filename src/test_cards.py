from card import Card
import random

class Cellar(Card):
    def __init__(self):
        super().__init__("action", 2)

    def run(self, player, game):
        # not checking all possibilities
        for card in player.hand:
            if card.type == 'vcard' \
                or card.type == 'curse':
                player.discard(card)

class CouncilRoom(Card):
    def __init__(self):
        super().__init__('action', 5)

    def run(self, player, game):
        player.draw(4) 
        player.buys += 1

class Festival(Card):
    def __init__(self):
        super().__init__('action', 5)

    def run(self, player, game):
        player.actions += 2
        player.buys += 1
        player.money += 2

class Laboratory(Card):
    def __init__(self):
        super().__init__("action", 5)

    def run(self, player, game):
        player.draw(2)
        player.actions += 1

class Market(Card):
    def __init__(self):
        super().__init__("action", 5)

    def run(self, player, game):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1

class Militia(Card):
    def __init__(self):
        super().__init__("action", 4, attack=True)

    def run(self, player, game):
        player.money += 2

        for p in game.players:
            # gotta offer them the choice tho
            # if they have a harbinger
            # there might be value to discarding?
            # hm...idk tho. if they kept cards,
            # they'd be discarded at end of turn. 
            if (p.has_moat or
                p == self):
                continue

            while len(p.hand) > 3:
                # random!!!
                choice = random.choice(p.hand)
                p.discard(choice)

class Moat(Card):
    def __init__(self):
        super().__init__("action", 2, reaction=True)

    def run(self, player, game):
        player.draw(2) 

# still need to implement the discard feature
class Poacher(Card):
    def __init__(self):
        super().__init__("action", 4)

    def run(self, player, game):
        player.draw(1)
        player.actions += 1
        player.money += 1

class Smithy(Card):
    def __init__(self):
        super().__init__("action", 4)

    def run(self, player, game):
        player.draw(3)

class Village(Card):
    def __init__(self):
        super().__init__("action", 3)

    def run(self, player, game):
        player.draw(1)
        player.actions += 2


# Treasure Cards
class Copper(Card):
    def __init__(self):
        super().__init__( 
          "treasure",
          0,
          value=1
        )

    def run(self, player, game):
        player.money += self.value

class Silver(Card):
    def __init__(self):
        super().__init__( 
          "treasure",
          3,
          value=2
        )

    def run(self, player, game):
        player.money += self.value

class Gold(Card):
    def __init__(self):
        super().__init__( 
          "treasure",
          6,
          value=3
        )

    def run(self, player, game):
        player.money += self.value


# Standard Victory Cards
class Estate(Card):
    def __init__(self):
        super().__init__( 
          "vcard",
          2,
          v_points=1
        )

class Duchy(Card):
    def __init__(self):
        super().__init__( 
          "vcard",
          5,
          v_points=3
        )

class Province(Card):
    def __init__(self):
        super().__init__( 
          "vcard",
          8,
          v_points=6
        )


# curses
class Curse(Card):
    def __init__(self):
        super().__init__( 
          "curse",
          0,
          v_points=-1
        )