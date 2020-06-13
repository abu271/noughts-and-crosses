board_state= [1,2,"X",4,5,6,7,8,9]

def draw():
  for i in range(3):
    print(" --- --- --- ")
    print("| {} | {} | {} |".format(*board_state[3*i:3*i+3]))
    print(" --- --- ---")

draw()
