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
        outRow = row < 0 or row >= self.size
        outCol = col < 0 or col >= self.size
        
        if outRow or outCol:
            return slot.get_slot_out()
        else:
             return self.matrix[row*self.size + col]
    def get_neighbornumber_by_slot(self, slot, slot_neighbor):
        if slot.row == slot_neighbor.row and slot.col - 1 == slot_neighbor.col:
            return 1 
        if slot.row - 1 == slot_neighbor.row and slot.col == slot_neighbor.col:
            return 2
        if slot.row == slot_neighbor.row and slot.col + 1 == slot_neighbor.col:
            return 3
        if slot.row  + 1 == slot_neighbor.row and slot.col == slot_neighbor.col:
            return 4

        if slot.row + 1 == slot_neighbor.row and slot.col - 1 == slot_neighbor.col:
            return 5 
        if slot.row - 1 == slot_neighbor.row and slot.col - 1 == slot_neighbor.col:
            return 6
        if slot.row - 1 == slot_neighbor.row and slot.col + 1 == slot_neighbor.col:
            return 7
        if slot.row + 1 == slot_neighbor.row and slot.col + 1 == slot_neighbor.col:
            return 8

        if slot.row - 2 == slot_neighbor.row and slot.col == slot_neighbor.col:
            return 9
        if slot.row + 2 == slot_neighbor.row and slot.col == slot_neighbor.col:
            return 10
        if slot.row == slot_neighbor.row and slot.col + 2 == slot_neighbor.col:
            return 11
        if slot.row == slot_neighbor.row and slot.col - 2 == slot_neighbor.col:
            return 12
    def get_slot_by_neighbornumber(self, slot, neighbornumber):
        row = slot.row
        col = slot.col
        if neighbornumber == 1:
            return self.get_slot_by_index(row,col - 1)
        if neighbornumber == 2:
            return self.get_slot_by_index(row - 1,col)
        if neighbornumber == 3:
            return self.get_slot_by_index(row,col + 1)
        if neighbornumber == 4:
            return self.get_slot_by_index(row + 1,col)
        if neighbornumber == 5:
            return self.get_slot_by_index(row + 1,col - 1)
        if neighbornumber == 6:
            return self.get_slot_by_index(row - 1,col - 1)
        if neighbornumber == 7:
            return self.get_slot_by_index(row - 1,col + 1)
        if neighbornumber == 8:
            return self.get_slot_by_index(row + 1,col + 1)
        if neighbornumber == 9:
            return self.get_slot_by_index(row - 2,col)
        if neighbornumber == 10:
            return self.get_slot_by_index(row + 2,col)
        if neighbornumber == 11:
            return self.get_slot_by_index(row,col + 2)
        if neighbornumber == 12:
            return self.get_slot_by_index(row,col - 2)

    def get_slots_by_adyacent(self, slot, neighbor):

        adyacent_neighborhood = []
        if neighbor == 1:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 1))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 5))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 6))
            return adyacent_neighborhood
        if neighbor == 2:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 2))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 6))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 7))
            return adyacent_neighborhood
        if neighbor == 3:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 3))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 7))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 8))
            return adyacent_neighborhood
        if neighbor == 4:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 4))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 5))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 8))
            return adyacent_neighborhood
        if neighbor == 5:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 1))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 4))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 5))
            return adyacent_neighborhood
        if neighbor == 6:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 1))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 2))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 6))
            return adyacent_neighborhood   
        if neighbor == 7:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 2))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 3))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 7))
            return adyacent_neighborhood
        if neighbor == 8:
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 3))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 4))
            adyacent_neighborhood.append(self.get_slot_by_neighbornumber(slot, 8))
            return adyacent_neighborhood      

    def get_slots_by_neighboring(self, slot):
        neighborhood = [
            self.get_slot_by_neighbornumber(slot, 1),
            self.get_slot_by_neighbornumber(slot, 2),
            self.get_slot_by_neighbornumber(slot, 3),
            self.get_slot_by_neighbornumber(slot, 4),
            self.get_slot_by_neighbornumber(slot, 5),
            self.get_slot_by_neighbornumber(slot, 6),
            self.get_slot_by_neighbornumber(slot, 7),
            self.get_slot_by_neighbornumber(slot, 8),
            self.get_slot_by_neighbornumber(slot, 9),
            self.get_slot_by_neighbornumber(slot, 10),
            self.get_slot_by_neighbornumber(slot, 11),
            self.get_slot_by_neighbornumber(slot, 12),
        ]
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
            rnd = random.randint(1,4)
            occupant = self.get_slot_by_neighbornumber(slot, rnd)

            if rnd == 1:
                neighbor = 12
            if rnd == 2:
                neighbor = 9
            if rnd == 3:
                neighbor = 10
            if rnd == 4:
                neighbor = 11
            
            if occupant.component == "empty" or occupant.component == "out":
                return
            if occupant.component != "BL":
                slot.component = occupant.component
                occupant.component = "empty"
                self.print_earth()

            if occupant.component == "BL" and self.get_slot_by_neighbornumber(slot, neighbor) == "S":
                slot.component = self.get_slot_by_neighbornumber(slot, neighbor).component
                self.get_slot_by_neighbornumber(slot, neighbor).component = "empty"
                self.print_earth()
                
    def do_second_motion(self):
        pass
    def do_third_motion(self):
        pass
    def do_production(self):
        k_list = self.get_slots_by_component("K")
        
        for k in k_list:
            neighboring = self.get_slots_by_neighboring(k)
            s_neighboring = list(filter(lambda slot: (slot.component == "S"), neighboring))

            candidates = []

            if self.get_slot_by_neighbornumber(k, 1) in s_neighboring and len(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 1)))) > 1:
                candidates.extend(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 1))))
            if self.get_slot_by_neighbornumber(k, 2) in s_neighboring and len(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 2)))) > 1:
                candidates.extend(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 2))))
            if self.get_slot_by_neighbornumber(k, 3) in s_neighboring and len(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 3)))) > 1:
                candidates.extend(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 3))))
            if self.get_slot_by_neighbornumber(k, 4) in s_neighboring and len(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 4)))) > 1:
                candidates.extend(list(filter(lambda slot: (slot.component == "S"), self.get_slots_by_adyacent(k, 4))))
            
            candidates = list(set(candidates))
            if len(candidates) == 0:
                return

            rdn_slot_L = random.choice(candidates)
            rdn_slot_S = random.choice(list(filter(lambda slot: (slot.component == "S" and slot != rdn_slot_L), self.get_slots_by_adyacent(k, self.get_neighbornumber_by_slot(k,rdn_slot_L)))))

            rdn_slot_L.component = "L"
            rdn_slot_S.component = "empty"

    def do_bond(self):
        free_link_list = self.get_slots_by_component("L")
        bond_link_list = self.get_slots_by_component("BL")


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
                marker = "x"
                color = 'k'
            plt.plot(slot.col, self.size - 1 - slot.row, marker, markersize=20, color = color)
        plt.show()