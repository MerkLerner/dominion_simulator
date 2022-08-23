from card import Card

class Market(Card):
    def __init__(self):
        super().__init__("action", 5)

    def run(self, player, game):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1

class Village(Card):
    def __init__(self):
        super().__init__("action", 3)

    def run(self, player, game):
        player.draw(1)
        player.actions += 2

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

class Laboratory(Card):
    def __init__(self):
        super().__init__("action", 5)

    def run(self, player, game):
        player.draw(2)
        player.action += 1

class Festival(Card):
    def __init__(self):
        super().__init__('action', 5)

    def run(self, player, game):
        player.actions += 2
        player.buys += 1
        player.money += 2

class CouncilRoom(Card):
    def __init__(self):
        super().__init__('action', 5)

    def run(self, player, game):
        player.draw(4) 
        player.buys += 1



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

if __name__ == "__main__":
    from player import Player
    from places import Piles
    from game import Game

    game = Game()
    piles = Piles()

    Markets = []
    for _ in range(10):
        Markets.append(Market())

    piles.kingdom_cards.append(Markets)
    game.piles = piles

    players = [
        Player([],[],[], game)
    ]

    game.players = players

    while True:
        for p in players:
            can_buy = []
            for card_stack in piles.kingdom_cards:
                # remember that there'll be a None
                # one pile depleted
                if card_stack[0].cost <= p.money:
                    can_buy.append(card_stack)

            print(p.money, can_buy, len( p.hand))

            break

        break