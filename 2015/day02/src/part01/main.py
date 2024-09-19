with open("2015/day02/src/part01/input.txt", "r") as input_file:
    data = input_file.read().splitlines()

sum = 0
for line in data:
   length, width, height = [int(x) for x in line.split("x")]
   lw = 2 * length * width
   wh = 2 * width * height
   hl = 2 * height * length
   area =  lw + wh + hl
   slack = min(lw, wh, hl) * 0.5
   sum = sum + area + slack

print(sum)