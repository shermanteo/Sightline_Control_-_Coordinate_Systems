# Direction Cosine Matrix (DCM)
# Rotation of the ECEF Coordinates to the Local Vertical Coordinates
# The rotation matrix will be rotating the coordinates in North-East-Down (NED) Convention

import numpy as np
from math import sin, cos


Latitude1 = float(input('Latitude of the target position:'))        # Latitude of the target position
Longitude1 = float(input('Longitude of the target position:'))      # Longitude of the target position
Altitude1 = float(input('Altitude of the target position:'))        # Altitude of the target position

Matrix_NED_1 = np.matrix ([[ -sin(Latitude1), 0, cos(Latitude1)],
                           [ 0, 1, 0], 
                           [ -cos(Latitude1), 0, -sin(Latitude1)]])
Matrix_NED_2 = np. matrix ([[ cos(Longitude1), sin(Longitude1), 0],
                            [ -sin(Longitude1), cos(Longitude1), 0],
                            [ 0, 0, 1]])

NED_Rotation_Matrix = Matrix_NED_1 * Matrix_NED_2
