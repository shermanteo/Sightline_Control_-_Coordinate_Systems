# Rotation Matrix in the Z-Axis (Yaw)

import numpy as np
from math import sin, cos

psi = float(input('Input the Yaw of the platform in Radians: '))

rot_z = np.matrix([[ cos(psi), -sin(psi), 0],
                   [ sin(psi), cos(psi), 0], 
                   [ 0, 0, 1]])