with open("2015/day02/src/part02/input.txt", "r") as input_file:
    data = input_file.read()

for line in data:
   listed = [int(x) for x in line.split("x")]
   listed.sort()
   short1, short2, short3 = listed
   perimeter = 2 * (short1 + short2)
   area = short1 * short2 * short3
   sum = sum + area + perimeter

print(sum)