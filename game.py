import utils
import board


def start_game():
  print("Welcome to a game of Noughts and Crosses")
  play_game = input("Would like to play a game? ")
  play_game = utils.is_yes(play_game)
  if play_game:
    players = utils.get_player_names()
    player_x = players["player_x"]
    player_o = players["player_o"]
    game_over = False
    while game_over:
      print("game started")
      # print board
      # player x goes first
      # manage player turns
      # update board based on players choice
      # after each turn check if anyone won
      # if no one won call it a draw
      # end game and ask if they want to play again
    else:
      print("Game Over")
  else:
    print("Okay come again")


start_game()
