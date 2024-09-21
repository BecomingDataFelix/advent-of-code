with open("2015/day03/src/part02/input.txt", "r") as input_file:
    data = input_file.read()

santaX, santaY, roboX, roboY = 0, 0, 0, 0
myset = set()
myset.add((0,0))
mapdict = {'^':1, '>': 1, '<': -1, 'v': -1, '\n':0}
for i, symbol in enumerate(data):
    if ((i+1) % 2) == 0:
        if (symbol in ['^', 'v']):
            roboX +=  mapdict[symbol]
        elif (symbol in ['<', '>']):
            roboY += mapdict[symbol]
        state = (roboX, roboY)
        myset.add(state)
        
    elif ((i+1) % 2) == 1:
        if (symbol in ['^', 'v']):
            santaX +=  mapdict[symbol]
        elif (symbol in ['<', '>']):
            santaY += mapdict[symbol]
        state = (santaX, santaY)
        myset.add(state)
    

print (myset)
print (len(myset))