# Direction Cosine Matrix (DCM)
# Rotation of the ECEF Coordinates to the Local Vertical Coordinates
# The rotation matrix will be rotating the coordinates in North-East-Down (NED) Convention

import numpy as np
from math import sin, cos

def ECEF_2_NED(X, Y, Z, Latitude, Longitude, Altitude):
  Matrix_NED_1 = np.matrix ([[ -sin(Latitude), 0, cos(Latitude)],
                             [ 0, 1, 0], 
                             [ -cos(Latitude), 0, -sin(Latitude)]])
  Matrix_NED_2 = np. matrix ([[ cos(Longitude), sin(Longitude), 0],
                              [ -sin(Longitude), cos(Longitude), 0],
                              [ 0, 0, 1]])
  NED_Rotation_Matrix = Matrix_NED_1 * Matrix_NED_2

  Coordinates_ECEF = np.matrix ([[ X ],
                            [ Y ], 
                            [ Z ]])

  NED_convention = NED_Rotation_Matrix * Coordinates_ECEF

  x = NED_convention[0][0] 
  y = NED_convention[1][0] 
  z = NED_convention[2][0] 
  
  return x, y, z
