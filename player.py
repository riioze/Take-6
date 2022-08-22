

class Player:
    def __init__(self):
        self.hand = []
        self.taken = []
    def __repr__(self):
        return 'hand : ' + str(self.hand) + ' ; taken : ' + str(sum([val for n,val in self.taken]))



class Human(Player):

    def play(self,table):
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
