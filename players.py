import utils

def assign_players():
  global player_x 
  global player_o 
  players = utils.get_player_names()
  player_o = players["player_o"]
  player_x = players["player_x"]

