import utils

class Player:
  def __init__(self, value, name):
    self.name = name
    self.type = value
    self.won = False
    self.turn = utils.true_or_false()