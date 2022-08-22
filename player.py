

class Player:
    def __init__(self):
        self.hand = []
        self.taken = []
    def __repr__(self):
        return 'hand : ' + str(self.hand) + ' ; taken : ' + str(sum([val for n,val in self.taken]))
