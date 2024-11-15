import re
from ctypes import c_int

import numpy as np
from numpy.ma.core import min_val, nonzero


def processCommands(input):
    action, x1, y1, x2, y2 =  re.search( r"(\w+) (\d+),(\d+) through (\d+),(\d+)", input).groups()
    return action, slice(int(x1), int(x2) + 1), slice(int(y1), int(y2)+1)


def gridAction(input):
  grid = np.zeros((1000,1000), dtype=np.int32)
  for command in input.split('\n'):
    action, slice1, slice2 = processCommands(command)
    if action == 'toggle':
      grid[slice1, slice2] += 2
    elif action == 'on':
      grid[slice1, slice2] += 1
    elif action == 'off':
      grid[slice1, slice2] = np.clip(grid[slice1, slice2] - 1, 0, None)

  return np.sum(grid)





if __name__ == '__main__':
  with open("input.txt", "r") as input_file:
    input = input_file.read()
  totalOn = gridAction(input)
  print(totalOn)