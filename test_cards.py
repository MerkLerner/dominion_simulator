from card import Card

class Market(Card):
    def __init__(self):
        super().__init__("attack","5")

    def run(self, player, target=None):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1

class Copper(Card):
    def __init__(self):
        super().__init__( 
          "money",
          0,
          value=1
        )

class Estate(Card):
    def __init__(self):
        super().__init__( 
          "vcard",
          2,
          v_points=1
        )

if __name__ == "__main__":
    from player import Player

    P = Player([],[],[])
    
    M = Market()
    P.play(M)
    print(P.actions)

    C = Copper()
    print(C.value)

    E = Estate()
    print(E.v_points)
