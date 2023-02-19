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
    
    def get_slots_by_neighboring(self, slot):
        pass
    
    def get_slots_by_component(self, component):
        earth = self.matrix
        slots = []

        for slot in earth:
            if slot.component == component:
                slots.append(slot)
        return slots
    
    def do_first_motion(self):
        empty_slots = self.get_slots_by_component("empty")
        
        for slot in empty_slots:
            print(f"x = {slot.row} y = {slot.col}")
            rnd = random.randint(1,4)
            # slot.move(rnd)
        pass
    def do_second_motion(self):
        pass
    def do_third_motion(self):
        pass
    def do_production(self):
        pass
    def do_bond(self):
        pass
    def do_rebond(self):
        pass

    def print_earth(self):
        plt.figure()
        plt.grid('on')
        #plt.axis('off')
        for slot in self.matrix:
            if(slot.component == "S"):
                marker = '8'
            elif(slot.component == "K"):
                marker = '*'
            elif(slot.component == "L"):
                marker = "s"
            elif(slot.component == "BL"):
                marker = "P"
            elif(slot.component == "empty"):
                marker = "bo"
            plt.plot(slot.row, slot.col, marker, markersize=10)
        plt.show()