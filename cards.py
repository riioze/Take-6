
cardlist = []
for x in range(1,105):
    if x == 55:
        y = 7
    elif x%11 == 0:
        y = 5
    elif x%10 == 0:
        y = 3
    elif x%10 == 5:
        y = 2
    else:
        y = 1
    cardlist.append((x,y))
