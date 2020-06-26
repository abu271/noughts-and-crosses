import utils
import players

class Board:
  state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  player_x = ""
  player_o = ""

  def update_board(self, num, value):
    num = int(num)
    index = Board.state.index(num)
    Board.state[index] = value
    self.draw()

  def three_in_a_row(self, value):
    if self.check_rows(value):
      return True
    elif self.check_columns(value):
      return True
    elif self.check_diagonals(value):
      return True
    else:
      return False

  @staticmethod
  def set_player_names(player_x, player_o):
    Board.player_x = player_x
    Board.player_o = player_o

  @staticmethod
  def draw():
    utils.clear_screen()
    print("X:{}  O:{}".format(Board.player_x, Board.player_o))
    for i in range(3):
      print(" --- --- --- ")
      print("| {} | {} | {} |".format(*Board.state[3*i:3*i+3]))
      print(" --- --- ---")

  @staticmethod
  def reset():
    Board.state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  def player_input(self, player):
    value = input("Your turn {} enter a number: ".format(player))
    while not utils.valid_number(value):
      value = input("{} please enter a number: ".format(player))
    while not self.position_available(value):
      value = input("{} that spot is taken try again: ".format(player))
    return value

  @staticmethod
  def position_available(position):
    position = int(position)
    if position in Board.state:
      return True
    else:
      return False

  @staticmethod
  def check_rows(value):
    first_row = []
    second_row = []
    third_row = []
    # populate the rows
    for x in range(0,3):
      first_row.append(Board.state[x])
    for y in range(3, 6):
      second_row.append(Board.state[y])
    for z in range(6, 9):
      third_row.append(Board.state[z])
    # check if any rows has three of the same value 
    if first_row.count(value) == 3:
      return True  
    elif second_row.count(value) == 3:
      return True  
    elif third_row.count(value) == 3:
      return True
    else:
      return False

  @staticmethod
  def check_columns(value):
    first_column = []
    second_column = []
    third_column = []
    # populate the columns
    for x in range(0,7,3):
      first_column.append(Board.state[x])
    for y in range(1,8,3):
      second_column.append(Board.state[y])
    for z in range(2,9,3):
      third_column.append(Board.state[z])
    # check if any columns has three of the same value 
    if first_column.count(value) == 3:
      return True
    elif second_column.count(value) == 3:
      return True
    elif third_column.count(value) == 3:
      return True
    else:
      return False

  @staticmethod
  def check_diagonals(value):
    diagonal_LR = [] 
    diagonal_RL = []
    # populate diagonal left to right(LR) and right to left (RL)
    for x in range(0,9,4):
      diagonal_LR.append(Board.state[x])
    for x in range(2, 8, 2):
      diagonal_RL.append(Board.state[x])
    # Check if any diagonals have three of the same value
    if diagonal_LR.count(value) == 3:
      return True
    elif diagonal_RL.count(value) == 3:
      return True
    else:
      return False

  @staticmethod
  def is_a_draw():
    numbers_only = list(filter(lambda x: isinstance(x, int), Board.state))
    number_of_moves_left = len(numbers_only)
    if number_of_moves_left == 0:
      return True
    else:
      return False
