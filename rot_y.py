# Rotation Matrix in the Y-Axis (Pitch)

import numpy as np
from math import sin, cos

theta = float(input('Input the Pitch of the platform in Radians: '))

rot_y = np.matrix([[ cos(theta), 0, sin(theta)],
                   [ 0, 1, 0], 
                   [ -sin(theta), 0, cos(theta)]])