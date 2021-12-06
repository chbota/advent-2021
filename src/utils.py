from functools import reduce
from os import path


def read_input(path, process = lambda x: x):
  res = []
  with open(path) as reader:
    line = reader.readline()
    while line != '':
      res.append(process(line.strip()))
      line = reader.readline()
  return res


def get_data_path(input_path):
 return path.join(path.dirname(__file__), f'./data/{input_path}')


def print_grid(grid):
  for x in range(len(grid)):
      printed_row = reduce(lambda acc, curr: f'{acc} {curr}', grid[x])
      print(printed_row)
