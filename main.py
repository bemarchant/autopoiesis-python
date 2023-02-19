import numpy as np
import random
import matplotlib.pylab as plt

nrow = 10
ncol = 10

class Earth:
    def __init__(self):
       self.nrow = 10
       self.ncol = 10
       self.matrix = []

    def init_earth(self):
        for row in np.arange(0,nrow):
            for col in np.arange(0,ncol):
                self.matrix.append(Component(row,col))
    def checkForLife(self):
        pass
    def printEarth(self):
        plt.figure()
        plt.grid('on')
        #plt.axis('off')
        for c in self.matrix:
            plt.plot(c.row, c.col, 'bo', markersize=10)
        plt.show()

class Substrate():
    pass
class Catalyst():
    pass
class Link():
    pass 
class BondedLink():
    pass

class Interaction():
    pass
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

def firstMotion(earth):
    for c in  earth.matrix:
        rnd = random.randint(1,4)
        c.move(rnd, earth)
def secondMotion(earth):
    pass
def thirdMotion(earth):
    pass

earth = Earth()
earth.init_earth()
earth.matrix[2]

firstMotion(earth)
earth.printEarth()