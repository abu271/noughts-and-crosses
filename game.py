import utils
import board
import players

def start_game():
  print("Welcome to a game of Noughts and Crosses")
  play_game = input("Would like to play? ")
  play_game = utils.is_yes(play_game)
  if play_game:
    players.assign_players()
    game_over = False
    player_x_turn = False
    player_x_won = False
    player_o_won = False
    board.draw()

    while not game_over:
      if player_x_turn:
        value = input("Your turn {} enter a number: ".format(players.player_x))
        while not utils.valid_number(value):
          value = input("{} please enter a number: ".format(players.player_x))
        while not board.position_available(value):
          value = input("{} that spot is taken try again: ".format(players.player_x))
        board.update_board(value, "X")
        player_x_won = board.three_in_a_row("X")
        player_x_turn = False
      else:
        value = input("Your turn {} enter a number: ".format(players.player_o))
        while not utils.valid_number(value):
          value = input("{} please enter a number: ".format(players.player_o))
        while not board.position_available(value):
          value = input("{} that spot is taken try again: ".format(players.player_o))
        board.update_board(value, "O")
        player_o_won = board.three_in_a_row("O")
        player_x_turn = True

      if player_x_won:
        print("THE WINNER IS {}".format(players.player_x))
        game_over = True
      elif player_o_won:
        print("THE WINNER IS {}".format(players.player_o))
        game_over = True
      else: 
        is_draw = board.is_a_draw()
        if is_draw:
          print("IT'S A DRAW!!")
          game_over = True

    else:
      print("Game Over")
  else:
    print("See you next time")


start_game()
