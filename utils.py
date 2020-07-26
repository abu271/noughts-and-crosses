import random

def is_yes(word):
  word = word.lower()
  word = word.replace(" ", "")
  if word in ["y", "yes"]:
    return True
  else:
    return False

def valid_number(num):
  is_digit = num.isdigit()
  if is_digit:
    num = int(num)
    within_range = 0 < num < 10 
    if within_range:
      return True
    else:
      print("Please select a number available on the board")
      return False
  else:
    return False

def clear_screen():
  print("\n" * 100)

def true_or_false():
  if random.randint(0, 1) == 0:
    return True
  else:
    return False

def start_game(text):
  word = input(text)
  return is_yes(word)

def print_win_message(player):
  print(f"THE WINNER IS {player}")

def get_column(matrix, index):
  return [row[index] for row in matrix]

def is_three(arrays, value):
  for row in arrays:
    if row.count(value) == 3:
      return True
  return False

def update_matrix(matrix, num, value):
    if num < 4:
      matrix[0]
      index = matrix[0].index(num)
      matrix[0][index] = value
      return matrix
    elif num < 7:
      matrix[1]
      index = matrix[1].index(num)
      matrix[1][index] = value
      return matrix
    else:
      matrix[2]
      index = matrix[2].index(num)
      matrix[2][index] = value
      return matrix

def get_names():
  player_o = input("Enter player O name: ")
  player_x = input("Enter player X name: ")
  players = {
    "X": player_x,
    "O": player_o
  }
  return players
