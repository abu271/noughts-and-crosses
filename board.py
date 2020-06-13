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
  