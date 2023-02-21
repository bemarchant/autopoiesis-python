import numpy as np
import random
import matplotlib.pylab as plt

from earth import * 
size = 3

earth = Earth(size)
earth.init_earth()
earth.print_earth()
earth.do_first_motion()
print(earth.get_slots_by_neighboring(earth.matrix[4]))