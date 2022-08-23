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
        can_buy = []
        for card_stack in piles.kingdom_cards:
            # remember that there'll be a None
            # one pile depleted
            if card_stack[0].cost <= p.money:
                can_buy.append(card_stack)

        print(p.money, can_buy, len( p.hand))

        break

    break

