import matplotlib.pylab as plt
import numpy as np
from slot import *

class Earth:
    def __init__(self,nrow,ncol):
       self.nrow = nrow
       self.ncol = ncol
       self.matrix = []

    def init_earth(self):
        for row in np.arange(0,self.nrow):
            for col in np.arange(0,self.ncol):
                self.matrix.append(slot(row,col))
    def check_life(self):
        pass
    
    def print_earth(self):
        plt.figure()
        plt.grid('on')
        #plt.axis('off')
        for c in self.matrix:
            if(c.type == "S"):
                marker = '8'
            elif(c.type == "K"):
                marker = '*'
            elif(c.type == "L"):
                marker = "s"
            else:
                marker = "P"
            plt.plot(c.row, c.col, marker, markersize=10)
        plt.show()