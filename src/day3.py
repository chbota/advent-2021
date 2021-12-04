from utils import read_input
from os import path
from functools import reduce


def sum_bits(acc, curr):
  for bit in range(0, len(curr)):
    try:
      acc[bit] = acc.get(bit, 0) + int(curr[bit])
    except:
      continue
  return acc

def most_common_bit(bit, bit_counts, input_length):
  if bit_counts[bit] > input_length / 2:
    return '1'
  elif bit_counts[bit] < input_length / 2:
    return '0'
  else:
    return None

def count_bits(input):
  summed_bits = reduce(sum_bits, input, {})
  bit_counts = [most_common_bit(bit, summed_bits, len(input)) for bit in range(0, len(summed_bits))]
  return bit_counts

def solve():
  input = read_input(path.join(path.dirname(__file__),'./data/day3.txt'))
  bit_counts = count_bits(input)

  # part 1
  gamma_rate = ''
  epsilon_rate = ''
  for bit in range(0, len(bit_counts)):
    gamma_rate += bit_counts[bit]
    epsilon_rate += '1' if bit_counts[bit] == '0' else '0'

  gamma_rate = int(gamma_rate, 2)
  epsilon_rate = int(epsilon_rate, 2)

  print(gamma_rate)
  print(epsilon_rate)
  print(gamma_rate * epsilon_rate)

  # part 2
  oxygen = input
  carbon = input
  
  for bit in range(0, len(bit_counts)):
    if len(oxygen) > 1:
      oxygen_counts = count_bits(oxygen)
      target_bit_val = '1' if oxygen_counts[bit] is None else oxygen_counts[bit]
      oxygen = list(filter(lambda x: x[bit] == target_bit_val, oxygen))

    if len(carbon) > 1:
      carbon_counts = count_bits(carbon)
      target_bit_val = '1' if carbon_counts[bit] is None else carbon_counts[bit]
      carbon = list(filter(lambda x: x[bit] != target_bit_val, carbon))


  if len(oxygen) != 1 or len(carbon) != 1:
    raise Exception('You did it wrong')

  oxygen_reading = int(oxygen[0], 2)
  carbon_reading = int(carbon[0], 2)

  print(oxygen_reading * carbon_reading)
