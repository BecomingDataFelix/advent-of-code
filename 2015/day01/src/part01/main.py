
with open("2015/day01/src/part01/input.txt", "r") as input_file:
    data = input_file.read()

x=0;    
for bracket in data:
    if (bracket =="("): 
        x= x+1
    elif (bracket == ")"):
        x= x-1

print(x)