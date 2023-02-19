class Component():
  def __init__(self, row, col):
    self.row = row
    self.col = col
  def getNeighbor(self):
    pass
  def move(self, number, earth):
        neighborComponent = earth.matrix[10*self.row + self.col]
        if(number == 1):
            self.col -= 1
        elif(number == 2):
            self.row -= 1
        elif(number == 3):
            self.col += 1
        else:
            self.row += 1