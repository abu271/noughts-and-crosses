import utils

board_state= [1,2,3,4,5,6,7,8,9]

def draw():
  for i in range(3):
    print(" --- --- --- ")
    print("| {} | {} | {} |".format(*board_state[3*i:3*i+3]))
    print(" --- --- ---")

def update_board(num, value):
  num = int(num)
  index = board_state.index(num)
  board_state[index] = value
  draw()

def position_available(position):
  position = int(position)
  if position in board_state:
    return True
  else:
    return False

def three_in_a_row(value):
  if check_rows(value):
    return True
  elif check_columns(value):
    return True
  elif check_diagonals(value):
    return True
  else:
    return False

def check_rows(value):
  first_row = []
  second_row = []
  third_row = []
  # populate the rows
  for x in range(0,3):
    first_row.append(board_state[x])
  for y in range(3, 6):
    second_row.append(board_state[y])
  for z in range(6, 9):
    third_row.append(board_state[z])
  # check if any rows has three of the same value 
  if first_row.count(value) == 3:
    return True  
  elif second_row.count(value) == 3:
    return True  
  elif third_row.count(value) == 3:
    return True
  else:
    return False

def check_columns(value):
  first_column = []
  second_column = []
  third_column = []
  # populate the columns
  for x in range(0,7,3):
    first_column.append(board_state[x])
  for y in range(1,8,3):
    second_column.append(board_state[y])
  for z in range(2,9,3):
    third_column.append(board_state[z])
  # check if any columns has three of the same value 
  if first_column.count(value) == 3:
    return True
  elif second_column.count(value) == 3:
    return True
  elif third_column.count(value) == 3:
    return True
  else:
    return False

def check_diagonals(value):
  diagonal_LR = [] 
  diagonal_RL = []
  # populate diagonal left to right(LR) and right to left (RL)
  for x in range(0,9,4):
    diagonal_LR.append(board_state[x])
  for x in range(2, 8, 2):
    diagonal_RL.append(board_state[x])
  # Check if any diagonals have three of the same value
  if diagonal_LR.count(value) == 3:
    return True
  elif diagonal_RL.count(value) == 3:
    return True
  else:
    return False

def is_a_draw():
  numbers_only = list(filter(lambda x: isinstance(x, int), board_state))
  number_of_moves_left = len(numbers_only)
  if number_of_moves_left == 0:
    return True
  else:
    return False
