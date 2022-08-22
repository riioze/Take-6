from player import *
from cards import *
from utils import *
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

    def turn(self):
        played = []
        for player in self.playerlist:
            played.append((player,player.play(self.table)))
        played.sort(key=lambda x:x[1][0])

        for player,card in played:
            tableh = higher(self.table)
            if card[0] < min(tableh):
                i = player.choose(card,self.table)
                player.taken+=self.table[i]
                self.table[i] = [card]
            else:
                maxi = -1
                maxx = -1
                for i in range(4):
                    if tableh[i] < card[0] and tableh[i] > maxx:
                        maxx = tableh[i]
                        maxi = i
                i = maxi
                if len(self.table[i]) == 5:
                    player.taken+=self.table[i]
                    self.table[i] = [card]
                else:
                    self.table[i].append(card)



        return self.table



    def __repr__(self):
        r = 'Players : \n'
        for x in range(len(self.playerlist)):
            r+='player {} : {}\n'.format(x+1,self.playerlist[x].__repr__())
        r+='Table : \n'
        for line in self.table:
            r+= str(line)+'\n'
        return r
