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
    board.draw()

    while not game_over:
      # after each turn check if anyone won
      # if no one won call it a draw
      # end game and ask if they want to play again
      if player_x_turn:
        value = input("Your turn {} enter a number: ".format(players.player_x))
        while not utils.valid_number(value):
          value = input("{} please enter a number: ".format(players.player_x))
        while not board.position_available(value):
          value = input("{} that spot is taken try again: ".format(players.player_x))
        board.update_board(value, "X")
        player_x_turn = False
      else:
        value = input("Your turn {} enter a number: ".format(players.player_o))
        while not utils.valid_number(value):
          value = input("{} please enter a number: ".format(players.player_o))
        while not board.position_available(value):
          value = input("{} that spot is taken try again: ".format(players.player_o))
        board.update_board(value, "O")
        player_x_turn = True
    else:
      print("Game Over")
  else:
    print("See you next time")


start_game()
