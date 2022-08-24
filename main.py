from game import *
from strategies import *
from utils import calc_points
if __name__ == '__main__':
    maingame = Game([Human(),AI(StratMini()),AI(StratMini()),AI(StratMaxi()),AI(StratMaxi())])

    print('Youre hand : ', maingame.playerlist[0].hand)


    print('\n'*5)


    for x in range(10):
        played = maingame.turn()
        print('you now have {} points'.format(calc_points(maingame.playerlist[0].taken)))

    for x in range(len(maingame.playerlist)):
        print('player {} : {} points'.format(x+1,calc_points(maingame.playerlist[x].taken)))
