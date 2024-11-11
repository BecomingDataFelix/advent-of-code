
def containSThreeVowels(input):
  vowels = ['a','e','i','o','u']
  vowelCount = 0
  for char in input:
    if char in vowels:
      vowelCount += 1
  
  if vowelCount >= 3:
    print(vowelCount)
    return True
  
  return False

def containsDoubleletter(input):
  for char in input:
    if char*2 in input:
      print(char*2)
      return True
  return False


def containsForbiddenString(input):
  forbidden = ['ab', 'cd', 'pq','xy' ]
  for item in forbidden:
    if item in input:
      return True
  return False


def isNiceString(input):
  return containSThreeVowels(input) and containsDoubleletter(input) and (not containsForbiddenString(input))
  

if __name__ == '__main__':
  with open("input.txt", "r") as input_file:
    input = input_file.read().splitlines()

  niceCount = 0
  for item in input:
    if isNiceString(item):
      niceCount += 1

  print(niceCount)