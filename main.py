import numpy as np
import random
import matplotlib.pylab as plt

from earth import * 
nrow = 3
ncol = 3

earth = Earth(nrow, ncol)
earth.init_earth()
earth.print_earth()
earth.do_first_motion()