import re

def containsTwoLettersRepeating(input):
  matchingRegex = re.search(r"(\w{2}).*?\1", input)
  return  matchingRegex


def containsOneRepeating(input):
  matchingRegex = re.search(r"(\w{1}).\1", input)
  return  matchingRegex


def isNiceString(input):
  return containsTwoLettersRepeating(input) and containsOneRepeating(input)




if __name__ == '__main__':
  with open("input.txt", "r") as input_file:
    input = input_file.read().splitlines()

  niceCount = 0
  for item in input:
    if isNiceString(item):
      niceCount += 1

  print(niceCount)