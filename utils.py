import random

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

def clear_screen():
  print("\n" * 100)

def true_or_false():
  if random.randint(0, 1) == 0:
    return True
  else:
    return False