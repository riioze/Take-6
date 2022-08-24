

class Player:
    """parent class for the player classes don't use it use Human ans AI classes instead"""
    def __init__(self):
        self.hand = []
        self.taken = []
    def __repr__(self):
        return 'hand : ' + str(self.hand) + ' ; taken : ' + str(sum([val for n,val in self.taken]))



class Human(Player):
    """Use an instance of this class to allow a human player to play"""

    def play(self,table):
        """called by the turn method of the game. Allow the human player to choose the card to play"""
        print('Here is the table')
        for line in table:
            print(line)
        print('Here is youre hand')
        print(self.hand)
        g = False
        while not g:
            number = int(input())
            for x in  range(len(self.hand)):
                n,val = self.hand[x]
                if n == number:
                    g = True
                    cardn = x
        return self.hand.pop(cardn)

    def choose(self,card,table):
        """called by the turn method of Game, allow the Human player to choose the column to put his card when it's bellow all the others"""
        print('card :',card)
        print('table : ')
        for line in table:
            print(line,'sum :',sum([val for n,val in line]))
        g = False
        while not g:
            r = int(input('choose a line by its num(between 1 and 4) : '))
            print(r)
            if r>0 and r<5:
                return int(r)-1

class AI(Player):
    """use this class to allow an AI to play"""
    def __init__(self,strategy):
        """The strategy argument must be an instance of the strat used and not the class itself"""
        self.hand = []
        self.taken = []
        self.strategy = strategy

    def play(self,table):
        """allow the AI to apply its strategy to play the card"""
        choosed = self.strategy.play(table,self.hand)
        for x in range(len(self.hand)):
            if choosed == self.hand[x]:
                c = x
        self.hand.pop(c)
        return choosed
    def choose(self,card,table):
        """allow the AI to apply its strategy to choose the column to put his card when it's bellow all the others"""
        return self.strategy.choose(card,table,self.hand)
