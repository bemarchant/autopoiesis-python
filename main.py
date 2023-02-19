import numpy as np
import random
import matplotlib.pylab as plt

from earth import * 
nrow = 10
ncol = 10

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

def first_motion(earth):
    for c in  earth.matrix:
        rnd = random.randint(1,4)
        c.move(rnd, earth)

earth = Earth(nrow, ncol)
earth.init_earth()
earth.matrix[2]

first_motion(earth)
earth.print_earth()