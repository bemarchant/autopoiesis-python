from earth import *
from slot import *

earth = Earth(5)
earth.init_earth("empty")
earth.matrix[0] = slot(0,0, "S")
earth.matrix[15] = slot(3,0, "S")
earth.matrix[18] = slot(3,3, "S")

counter = 0
while counter < 1:
    earth.print_earth()
    earth.do_first_motion()
    #earth.do_production()random.randint(1,4)
    counter += 1
    earth.print_earth()