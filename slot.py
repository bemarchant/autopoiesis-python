import random

def get_rdn_component():
    rnd = random.randint(1,3)
    if rnd == 1:
        return "S"
    if rnd == 2:
        return "K"  
    return "empty"

class slot():
  def __init__(self, row, col, component):
    self.row = row
    self.col = col
    # self.component = get_rdn_component() #S, K, L, BL or empty
    self.component = component #S, K, L, BL or empty
  
  def get_slot_out():
    return slot(-1,-1,"out")
  def get_neighborhood(self):
    pass
  def move(self, number):
        # print(f"row : {self.row} col: {self.col}")
        if(number == 1):
            self.col -= 1
        elif(number == 2):
            self.row -= 1
        elif(number == 3):
            self.col += 1
        else:
            self.row += 1
            