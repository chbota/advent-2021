from functools import reduce
from os import path
from utils import read_input


# count all increasing vals
def count_increasing(input, window_size):
  increasing = 0
  window = []

  for depth in input:
    if len(window) == window_size:
      old_sum = reduce(lambda x, y: x + y, window)
      window.pop(0)
      window.append(depth)
      new_sum = reduce(lambda x, y: x + y, window)

      if new_sum > old_sum:
        increasing = increasing + 1
    else:
      window.append(depth)
  
  return increasing


def solve():
  input_path = path.join(path.dirname(__file__), 'data/day1.txt')
  input = read_input(input_path)
    
  print('day 1 part 1: {}'.format(
    count_increasing(input, 1)
  ))

  print('day 1 part 2: {}'.format(
    count_increasing(input, 3)
  ))
