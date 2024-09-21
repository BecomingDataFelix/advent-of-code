with open("2015/day03/src/part01/input.txt", "r") as input_file:
    data = input_file.read()

stateX, stateY = 0, 0
myset = set()
myset.add((0,0))
mapdict = {'^':1, '>': 1, '<': -1, 'v': -1, '\n':0}
for symbol in data:
    # print(f' {state} + { mapdict[symbol] } ={state + mapdict[symbol]}' )
    if (symbol in ['^', 'v']):
        stateX +=  mapdict[symbol]
    elif (symbol in ['<', '>']):
        stateY += mapdict[symbol]
    state = (stateX, stateY)
    myset.add(state)


print (myset)
print (len(myset))