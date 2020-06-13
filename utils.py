def get_player_names():
  players = {
    "player_x": '',
    "player_o": ''
  }
  players["player_x"] = input("Enter player X name: ")
  players["player_o"] = input("Enter player O name: ")
  return players


def is_yes(word):
  word.lower()
  word = word.replace(" ", "")
  if word in ["y", "yes"]:
    return True
  else:
    return False
