from utils import print_grid, read_input, get_data_path

import re

# y = mx + b
# m = y2 - y1 / x2 - x1

def parse_line(line):
  if not line:
    return None

  match = re.search(r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)', line)
  if not match:
    raise Exception(f'Parsing failed: {line}')

  return ((int(match.group('x1')), int(match.group('y1'))), (int(match.group('x2')), int(match.group('y2'))))

def line_function(line):
  ((x1, y1), (x2, y2)) = line
  slope = (y2 - y1) / (x2 - x1)
  b = y1 - slope * x1
  return lambda x: slope * x + b


def draw_lines(space, point_pairs):
  for pair in point_pairs:
    ((x1,y1), (x2,y2)) = pair

    if x1 == x2:
      for y in range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1):
          space[x1][y] += 1
    else:
      line_func = line_function(pair)
      for x in range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1):
        space[x][round(line_func(x))] += 1


def solve():
  input = read_input(get_data_path('day5.txt'))

  point_pairs = filter(lambda x: x is not None, map(parse_line, input))
  space = [[0 for y in range(1000)] for x in range(1000)]

  draw_lines(space, point_pairs)

  num_dangerous = 0
  for row in space:
    for point in row:
      if point >= 2:
        num_dangerous += 1

  print(f'day 5 part 1 {num_dangerous}')
