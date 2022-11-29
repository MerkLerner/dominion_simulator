'''
how tf to do cards that are played on oter peoples turns except i think that 
the only ones 
'''

from player import Player
from places import Piles
from game import Game
from test_cards import *

game = Game()

# # cuidado hombre
# Markets = []
# for _ in range(10): 
#     Markets.append(Market())

# piles.kingdom_cards.append(Markets)

# 

while True:
    for p in game.players:
        p.action_phase()
        p.buy_phase()
        p.clean_up()
        break
    break

#  wee wooo
p1 = Player([],[],[],game)
p2 = Player([],[],[],game)
game.players = {p1, p2}

p1.play(Cellar(), mode="test")

p1.play(CouncilRoom(), mode="test")

p1.play(Festival(), mode="test")

p1.play(Laboratory(), mode="test")

p1.play(Market(), mode="test")

p1.play(Militia(), mode="test")

p1.play(Moat(), mode="test")

p1.play(Village(), mode="test")

p1.play(Poacher(), mode="test")

p1.play(Smithy(), mode="test")

p1.play(Copper(), mode="test")

p1.play(Silver(), mode="test")

p1.play(Gold(), mode="test")