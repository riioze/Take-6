from game import *


if __name__ == '__main__':
    maingame = Game([Human(),Human()])
    print(maingame)

    for x in range(10):
        print(maingame.turn())
