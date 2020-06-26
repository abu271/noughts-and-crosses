import utils
from board import Board

def start_game():
  print("Welcome to a game of Noughts and Crosses")
  play_game = input("Would like to play? ")
  play_game = utils.is_yes(play_game)
  board = Board()
  
  while play_game:
    player_o = input("Enter player O name: ")
    player_x = input("Enter player X name: ")
    board.set_player_names(player_x, player_o)
    player_x_turn = utils.true_or_false()
    player_x_won = False
    player_o_won = False
    game_over = False
    board.reset()
    board.draw()

    while not game_over:

      if player_x_turn:
        value = board.player_input(player_x)
        board.update_board(value, "X")
        player_x_won = board.three_in_a_row("X")
        player_x_turn = False
      else:
        value = board.player_input(player_o)
        board.update_board(value, "O")
        player_o_won = board.three_in_a_row("O")
        player_x_turn = True

      if player_x_won:
        print("THE WINNER IS {}".format(player_x))
        game_over = True
      elif player_o_won:
        print("THE WINNER IS {}".format(player_o))
        game_over = True
      else: 
        is_draw = board.is_a_draw()
        if is_draw:
          print("IT'S A DRAW!!")
          game_over = True

    play_game = input("Would like to play again? ")
    play_game = utils.is_yes(play_game)

start_game()
