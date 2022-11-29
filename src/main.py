'''
how tf to do cards that are played on oter peoples turns except i think that 
the only ones 
'''

from player import Player
from places import Piles
from game import Game
from test_cards import *
import traceback


game = Game(2)

while True:
    try:
        for p in game.players:
            print(p.get_state())

            p.action_phase()
            input()
            
            print(p.get_state())
            p.buy_phase()
            input()

            print(p.get_state())
            p.clean_up()
            input()
    except Exception as E:
        print('game over!')
        traceback.print_exc()
        print(E)
        print(E.__traceback__.tb_frame)

        again = input('again?')
        if again.lower()[0] != 'y':
            print('bye now')
            break