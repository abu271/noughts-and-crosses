import utils
from board import Board
from player import Player

def start_game():
  print("Welcome to a game of Noughts and Crosses")
  play_game = utils.start_game("Would like to play? ")
  
  while play_game:
    players = utils.get_names()
    player_x = Player("X", players["X"])
    player_o = Player("O", players["O"])
    game_over = False
    board = Board()
    board.reset()
    board.draw()

    while not game_over:
      if player_x.turn:
        board.player_move(player_x)
        player_x.won = board.three_in_a_row("X")
      else:
        board.player_move(player_o)
        player_o.won = board.three_in_a_row("O")
      
      player_x.turn = not player_x.turn

      if player_x.won:
        utils.print_win_message(player_x.name)
        game_over = True
      elif player_o.won:
        utils.print_win_message(player_o.name)
        game_over = True
      else: 
        is_draw = board.is_a_draw()
        if is_draw:
          print("IT'S A DRAW!!")
          game_over = True

    play_game = utils.start_game("Would like to play again? ")

start_game()
