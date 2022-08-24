from player import *
from cards import *
from utils import *
from random import shuffle
class Game:

    """
    Class managing all the game after creating the instance use the method turn to play
    """

    def __init__(self,playerlist):
        self.playerlist = playerlist
        self.deck = [e for e in cardlist]
        self.distribute()



    def distribute(self):
        """
        method used to distribute randomly the cards to the players
        don't used it it's automatically called at the creation of the instance
        """
        shuffle(self.deck)
        for player in self.playerlist:
            for x in range(10):
                player.hand.append(self.deck.pop())
        self.table = []
        for x in range(4):
            self.table.append([self.deck.pop()])

    def turn(self):
        """method to call to simulate a turn"""
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



        return played



    def __repr__(self):
        """called on print"""
        r = 'Players : \n'
        for x in range(len(self.playerlist)):
            r+='player {} : {}\n'.format(x+1,self.playerlist[x].__repr__())
        r+='Table : \n'
        for line in self.table:
            r+= str(line)+'\n'
        return r
