
from functools import reduce
from utils import read_input, get_data_path


CALLED_NUMBER = 'XX'

# Bingo
# 0,0 0,1 0,2 0,3 0,4
# 1,0 1,1 1,2 1,3 1,4
# 2,0 2,1 2,2 2,3 2,4
# 3,0 3,1 3,2 3,3 3,4
# 4,0 4,1 4,2 4,3 4,4

def call_number(board, number):
  for x in range(len(board)):
    for y in range(len(board[x])):
      if board[x][y] == number:
        board[x][y] = CALLED_NUMBER


def check_board(board):
  for i in range(len(board)):
    # check horizontal
    if all([board[i][y] == CALLED_NUMBER for y in range(5)]):
      return True # winner

    # check vertical
    if (all([board[x][i] == CALLED_NUMBER for x in range(5)])):
          return True # winner

  return False


def parse_boards(boards):
  parsed = []
  current = []

  for line in boards:
    if line == '':
      continue

    current.append(line.split())

    if len(current) == 5:
      parsed.append(current)
      current = []

  return parsed

def print_board(board):
  for x in range(len(board)):
      printed_row = reduce(lambda acc, curr: f'{acc} {curr}', board[x])
      print(printed_row)


def play_game(boards, numbers):
  winners = []
  for number in numbers:
    for board in boards:
      if check_board(board):
        continue

      call_number(board, number)
      # print_board(board)
      # print('')
      if check_board(board):
        winners.append((board, number))
  return winners

def sum_board(board):
  summed_board = 0
  for x in range(len(board)):
    for y in range(len(board)):
      if board[x][y] == CALLED_NUMBER:
        continue
      summed_board += int(board[x][y])
  return summed_board

def solve():
  input = read_input(get_data_path('day4.txt'))

  numbers = input[0].split(',')
  boards = parse_boards(input[2:])

  winners = play_game(boards, numbers)

  if len(winners):
    (first_winner, first_winner_number) = winners[0]
    winner_sum = sum_board(first_winner)
    print(f'day 4 part 1 {winner_sum},{first_winner_number},{winner_sum * int(first_winner_number)}')
    
    (last_winner, last_winner_number) = winners[len(winners) - 1]
    last_winner_sum = sum_board(last_winner)
    print(f'day 4 part 2 {last_winner_sum},{last_winner_number},{last_winner_sum * int(last_winner_number)}')


