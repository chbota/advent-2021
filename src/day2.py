from utils import read_input
from os import path



def solve():
  input = read_input(path.join(path.dirname(__file__), './data/day2.txt'))

  position = 0
  depth = 0

  for instr in input:
    [direction, magnitude] = instr.split(' ')

    if direction == 'forward':
      position = position + int(magnitude)
    elif direction == 'down':
      depth = depth + int(magnitude)
    elif direction == 'up':
      depth = depth - int(magnitude)
    else:
      raise Exception('unknown direction {}'.format(direction))

  print('day 2 part 1: {}'.format(
    position * depth
  ))

  position = 0
  depth = 0
  aim = 0

  for instr in input:
      [direction, magnitude] = instr.split(' ')

      if direction == 'forward':
        position = position + int(magnitude)
        depth = depth + aim * int(magnitude)
      elif direction == 'down':
        aim = aim + int(magnitude)
      elif direction == 'up':
        aim = aim - int(magnitude)
      else:
        raise Exception('unknown direction {}'.format(direction))

  print('day 2 part 2: {}'.format(
    position * depth
  ))
