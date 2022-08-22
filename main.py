from game import *
from strategies import *
import os
if __name__ == '__main__':
    maingame = Game([Human(),AI(StratMini())])

    print('Youre hand : ', maingame.playerlist[0].hand)


    print('\n'*5)


    for x in range(10):
        played = maingame.turn()
        print('you now have {} points'.format(sum([val for n,val in maingame.playerlist[0].taken])))
