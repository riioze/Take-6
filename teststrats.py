from game import *
from strategies import *
from utils import calc_points


if __name__ == '__main__':
    points = [0,0]
    for i in range(100):
        maingame = Game([AI(StratMini()),AI(StratMini()),AI(StratMaxi()),AI(StratMaxi())])

        for x in range(10):
            maingame.turn()

        for x in range(len(maingame.playerlist)):
            print('player {} : {} points'.format(x+1,calc_points(maingame.playerlist[x].taken)))

        for x in range(2):
            for y in range(2):
                points[x]+=calc_points(maingame.playerlist[2*x+y].taken)
    print([p/200 for p in points])
