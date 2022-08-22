from player import *
from cards import *
from random import shuffle
class Game:
    def __init__(self,playerlist):
        self.playerlist = playerlist
        self.deck = [e for e in cardlist]
        self.distribute()



    def distribute(self):
        shuffle(self.deck)
        for player in self.playerlist:
            for x in range(10):
                player.hand.append(self.deck.pop())
        self.table = []
        for x in range(4):
            self.table.append([self.deck.pop()])


    def __repr__(self):
        r = 'Players : \n'
        for x in range(len(self.playerlist)):
            r+='player {} : {}\n'.format(x+1,self.playerlist[x].__repr__())
        r+='Table : \n'
        for line in self.table:
            r+= str(line)+'\n'
        return r
