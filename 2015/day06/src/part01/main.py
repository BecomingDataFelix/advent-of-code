import re

import numpy as np

def processCommands(input):
    action, x1, y1, x2, y2,  =  re.search( "(\w+) (\d+),(\d+) through (\d+),(\d+)", input).group()
    return action, slice(int(x1), int(x2) + 1), slice(int(y1), int(y2)+1)


def gridAction(input):
  grid = np.zeros((1000,1000), dtype=np.bool)
  for command in input.split('\n'):
    action, slice1, slice2 = processCommands(command)
    if action == 'toggle':
      grid[slice1, slice2] ^= True
    elif action == 'on':
      grid[slice1, slice2] = 1
    elif action == 'off':
      grid[slice1, slice2] = 0

  return sum(grid)





if __name__ == '__main__':
  with open("input.txt", "r") as input_file:
    input = input_file.read()

  totalOn = gridAction(input)

  print(totalOn)