import tango
import numpy as np
import time


pi_x = tango.DeviceProxy('B318A-EA01/CTL/PI_X')
x_pos = np.arange(-50, 50, 1)

for p in x_pos:
    pi_x.Position = p
    time.sleep(0.005)
    print(pi_x.PosError)
    print(pi_x.state())