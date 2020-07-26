import utils

class Board:
  state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  def update_board(self, num, player_type):
    num = int(num)
    Board.state = utils.update_matrix(Board.state, num, player_type)
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

  def player_move(self, player):
    num = self.player_input(player.name)
    self.update_board(num, player.type)

  @staticmethod
  def draw():
    utils.clear_screen()
    for i in range(3):
      print(" --- --- --- ")
      print(f"| {Board.state[i][0]} | {Board.state[i][1]} | {Board.state[i][2]} |")
      print(" --- --- ---")

  @staticmethod
  def reset():
    Board.state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  
  def player_input(self, name):
    num = input(f"Your turn {name} enter a number: ")
    while not utils.valid_number(num):
      num = input(f"{name} please enter a number: ")
    while not self.position_available(num):
      num = input(f"{name} that spot is taken try again: ")
    return num

  @staticmethod
  def position_available(position):
    position = int(position)
    for i in range(3):
      if position in Board.state[i]:
        return True
    return False

  @staticmethod
  def check_rows(value):
    first_row = Board.state[0]
    second_row = Board.state[1]
    third_row = Board.state[2]
    arrays = [first_row, second_row, third_row]
    return utils.is_three(arrays, value)

  @staticmethod
  def check_columns(value):
    first_column = utils.get_column(Board.state, 0)
    second_column = utils.get_column(Board.state, 1)
    third_column = utils.get_column(Board.state, 2)
    arrays = [first_column, second_column, third_column]
    return utils.is_three(arrays, value)

  @staticmethod
  def check_diagonals(value):
    first_column = utils.get_column(Board.state, 0)
    second_column = utils.get_column(Board.state, 1)
    third_column = utils.get_column(Board.state, 2)
    diagonal_LR = [first_column[0], second_column[1], third_column[2]] 
    diagonal_RL = [third_column[2], second_column[1],first_column[0]]
    arrays = [diagonal_LR, diagonal_RL]
    return utils.is_three(arrays, value)

  @staticmethod
  def is_a_draw():
    number_of_moves_left = 0
    for i in range(3):
      numbers_only = list(filter(lambda x: isinstance(x, int), Board.state[i]))
      number_of_moves_left += len(numbers_only)
    if number_of_moves_left == 0:
      return True
    else:
      return False
