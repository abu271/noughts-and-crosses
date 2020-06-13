def get_player_names():
  players = {
    "player_x": '',
    "player_o": ''
  }
  players["player_x"] = input("Enter player X name: ")
  players["player_o"] = input("Enter player O name: ")
  return players


def is_yes(word):
  word = word.lower()
  word = word.replace(" ", "")
  if word in ["y", "yes"]:
    return True
  else:
    return False

def valid_number(num):
  is_digit = num.isdigit()
  if is_digit:
    num = int(num)
    within_range = 0 < num < 10 
    if within_range:
      return True
    else:
      return False
  else:
    return False
     