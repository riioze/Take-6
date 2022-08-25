from random import choice,randint

class StratMini:
    def play(self,table,hand):
        mini = 105
        for n,val in hand:
            if n < mini:
                mini = n
                choosed = n,val
        return choosed
    def choose(self,card,table,hand):
        mini = 1000
        for x in range(len(table)):
            s = sum([val for n,val in table[x]])
            if s<mini:
                mini = s
                c=x
        return c

class StratMaxi:
    def play(self,table,hand):
        maxi = 0
        for n,val in hand:
            if n > maxi:
                maxi = n
                choosed = n,val
        return choosed
    def choose(self,card,table,hand):
        mini = 1000
        for x in range(len(table)):
            s = sum([val for n,val in table[x]])
            if s<mini:
                mini = s
                c=x
        return c

class StratRandom:
        def play(self,table,hand):
            return choice(hand)
        def choose(self,card,table,hand):
            return randint(0,3)
