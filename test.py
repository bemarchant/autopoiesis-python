from earth import *
from slot import *

earth = Earth(5)
earth.init_earth("empty")
earth.matrix[0] = slot(0,0, "S")
# earth.matrix[1] = slot(0,1, "S")
# earth.matrix[2] = slot(0,2, "S")
# earth.matrix[3] = slot(0,3, "S")
# earth.matrix[4] = slot(0,4, "S")
# earth.matrix[5] = slot(1,0, "S")
# earth.matrix[6] = slot(1,1, "empty")
# earth.matrix[7] = slot(1,2, "S")
# earth.matrix[8] = slot(1,3, "empty")
# earth.matrix[9] = slot(1,4, "S")
# earth.matrix[10] = slot(2,0, "S")
# earth.matrix[11] = slot(2,1, "S")
# earth.matrix[12] = slot(2,2, "K")
# earth.matrix[13] = slot(2,3, "empty")
# earth.matrix[14] = slot(2,4, "S")
# earth.matrix[15] = slot(3,0, "S")
# earth.matrix[16] = slot(3,1, "S")
# earth.matrix[17] = slot(3,2, "S")
# earth.matrix[18] = slot(3,3, "S")
# earth.matrix[19] = slot(3,4, "S")
# earth.matrix[20] = slot(4,0, "S")
# earth.matrix[21] = slot(4,1, "S")
# earth.matrix[22] = slot(4,2, "S")
# earth.matrix[23] = slot(4,3, "S")
# earth.matrix[24] = slot(4,4, "S")

counter = 0
while counter < 2:
    earth.print_earth()
    earth.do_first_motion()
    #earth.do_production()
    counter += 1