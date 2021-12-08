from utils import data, read_input

def simulate_fish_naive(fish, days):
  current_fishes = fish
  for _ in range(days):
    new_fish = []
    for fishy in current_fishes:
      if fishy == 0:
        new_fish.extend([6, 8])
      else:
        new_fish.append(fishy - 1)
    current_fishes = new_fish
  return len(current_fishes)

def simulate_fish(fish, days):
  fish_counts = [0 for x in range(9)]
  for fishy in fish:
    fish_counts[fishy] += 1

  for _ in range(days):
    parents = fish_counts[0]
    fish_counts = fish_counts[1:]
    # first add the new fishes at the end
    fish_counts.append(parents)
    # then put the parents back in
    fish_counts[6] += parents

  return sum(fish_counts)


def plot_fish_population(fish, x):
  res = [x, len(simulate_fish_naive(fish, x))]
  print(f'{x} - done {res[1]}')
  return res

def solve():
  input = read_input(data('day6.txt'))

  fish = [int(x) for x in input[0].split(',')]

  print(f'day 6 pt 1 {simulate_fish(fish, 80)}')
  print(f'day 6 pt 2 {simulate_fish(fish, 256)}')

