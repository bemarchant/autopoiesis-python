class component():
  def __init__(self, slot):
    self.slot = slot
    self.type = "S" #S, K, L, BL or empty
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