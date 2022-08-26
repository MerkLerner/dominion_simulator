'''
how tf to do cards that are played on oter peoples turns except i think that 
the only ones 
'''

from player import Player
from places import Piles
from game import Game
from test_cards import *

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
        p.action_phase()
        p.buy_phase()
        p.clean_up()
        break
    break

