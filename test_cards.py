from card import Card

class Market(Card):
    def __init__(self):
        print(self, super())
        super().__init__( 
        "action",
        5,
        False
        )

    def run(self, player, target=None):
        player.draw(1)
        player.actions += 1
        player.buys += 1
        player.money += 1

if __name__ == "__main__":
    from player import Player

    P = Player([],[],[])
    M = Market()

    P.play(M)

    print(P.actions)