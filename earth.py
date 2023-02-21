import matplotlib.pylab as plt
import numpy as np
from slot import *

class Earth:
    def __init__(self,size):
       self.size = size
       self.matrix = []

    def init_earth(self):
        for row in np.arange(0,self.size):
            for col in np.arange(0,self.size):
                self.matrix.append(slot(row,col, "S"))
            
    def check_life(self):
        pass
    
    def get_slot_by_index(self, row, col):
        outRight = row*self.size + col < 0
        outLeft = row*self.size + col >= self.size**2
        
        if outRight or outLeft:
            return slot.get_slot_out()
        else:
             return self.matrix[row*self.size + col]

    def get_slots_by_neighboring(self, slot):
        row = slot.row
        col = slot.col
        neighborhood = []
        
        neighbor_1 = self.get_slot_by_index(row,col - 1)
        neighbor_2 = self.get_slot_by_index(row - 1,col)
        neighbor_3 = self.get_slot_by_index(row,col + 1)
        neighbor_4 = self.get_slot_by_index(row + 1,col)
       
        neighbor_5 = self.get_slot_by_index(row + 1,col - 1)
        neighbor_6 = self.get_slot_by_index(row - 1,col - 1)
        neighbor_7 = self.get_slot_by_index(row - 1,col + 1)
        neighbor_8 = self.get_slot_by_index(row + 1,col + 1)

        neighbor_9 = self.get_slot_by_index(row - 2,col)
        neighbor_10 = self.get_slot_by_index(row,col + 2)
        neighbor_11 = self.get_slot_by_index(row + 2,col)
        neighbor_12 = self.get_slot_by_index(row,col - 2)

        neighborhood = [neighbor_1, 
        neighbor_2, 
        neighbor_3, 
        neighbor_4, 
        neighbor_5, 
        neighbor_6, 
        neighbor_7, 
        neighbor_8,
        neighbor_9,
        neighbor_10,
        neighbor_11,
        neighbor_12]

        return neighborhood
    
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
                color = 'k'
            elif(slot.component == "K"):
                marker = '*'
                color = 'k'
            elif(slot.component == "L"):
                marker = "s"
                color = 'k'
            elif(slot.component == "BL"):
                marker = "P"
                color = 'k'
            elif(slot.component == "empty"):
                marker = "bo"
                color = 'k'
            plt.plot(slot.row, slot.col, marker, markersize=20, color = color)
        plt.show()