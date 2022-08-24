
def calc_points(cardlist):
    return sum([val for n,val in cardlist])

def higher(table):
    r = []
    for line in table:
        r.append(line[-1][0])
    return r
