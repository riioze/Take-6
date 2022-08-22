

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
