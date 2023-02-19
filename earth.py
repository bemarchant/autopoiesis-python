import matplotlib.pylab as plt
import numpy as np
from component import *

class Earth:
    def __init__(self,nrow,ncol):
       self.nrow = nrow
       self.ncol = ncol
       self.matrix = []

    def init_earth(self):
        for row in np.arange(0,self.nrow):
            for col in np.arange(0,self.ncol):
                self.matrix.append(Component(row,col))
    def check_life(self):
        pass
    
    def print_earth(self):
        plt.figure()
        plt.grid('on')
        #plt.axis('off')
        for c in self.matrix:
            plt.plot(c.row, c.col, 'bo', markersize=10)
        plt.show()