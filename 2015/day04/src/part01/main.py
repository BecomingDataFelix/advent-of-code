import hashlib
with open("2015/day05/src/part01/input.txt", "r") as input_file:
    data = input_file.read()

for i in range(1, 10000000):
    hash = hashlib.md5((data + str(i)).encode())
    if str(hash.hexdigest())[:5] == '00000':
        print(i)
        break
    else: print(str(hash.hexdigest())[:5])