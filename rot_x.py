# Rotation Matrix in the X-Axis (Roll)

import numpy as np
from math import sin, cos

phi = float(input('Input the Roll of the platform in Radians: '))

rot_x = np.matrix([[ 1, 0, 0],
                   [ 0, cos(phi), -sin(phi)], 
                   [ 0, sin(phi), cos(phi)]])
