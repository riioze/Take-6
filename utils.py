
def calc_points(cardlist):
    """return the total points of a list of cards"""
    return sum([val for n,val in cardlist])

def higher(table):
    """return the number of the last (so higher) card of each column of the table"""
    r = []
    for line in table:
        r.append(line[-1][0])
    return r
