with open("2015/day01/src/part02/input.txt", "r") as input_file:
    data = input_file.read()

x=0;    
for index, bracket in enumerate(data):
    if (bracket =="("): 
        x= x+1
    elif (bracket == ")"):
        x= x-1
    
    if (x==-1):
	    print(index+1); break
