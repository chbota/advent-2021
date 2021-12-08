from utils import read_input, data

def calc_distances(input, candidate, cost):
  return [cost(x, candidate) for x in input]

def find_best_meeting_spot(crabs, cost):
  candidate_spots = list(range(min(crabs), max(crabs)))
  crab_distances = [calc_distances(crabs, x, cost) for x in candidate_spots]
  summed_distances = [sum(distances) for distances in crab_distances]
  min_distance = min(summed_distances)
  return (candidate_spots[summed_distances.index(min_distance)], min_distance)

def linear_cost(x, y):
  return abs(x - y)

def increasing_cost(x, y):
  return 0 if x == y else sum(range(abs(x - y) + 1))

def solve():
  crabs = [int(x) for x in read_input(data('day7.txt'))[0].split(',')]

  (first_meeting_spot, first_fuel_cost) = find_best_meeting_spot(crabs, lambda x, y: abs(x - y))
  print(f'day 7 part 1 meet at {first_meeting_spot}, {first_fuel_cost}')

  (second_meeting_spot, second_fuel_cost) = find_best_meeting_spot(crabs, increasing_cost)
  print(f'day 7 part 2 meet at {second_meeting_spot}, {second_fuel_cost}')
