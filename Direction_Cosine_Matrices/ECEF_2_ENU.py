# Direction Cosine Matrix (DCM)
# Rotation of the ECEF Coordinates to the Local Vertical Coordinates
# The rotation matrix will be rotating the coordinates in East-North-Up (ENU) Convention
# X, Y, Z are the coordinates input in ECEF 
# Output will be x, y, z which are the ECEF coordinates but in ENU Convention

import numpy as np
from math import sin, cos

def ECEF_2_NED(X, Y, Z, Latitude, Longitude, Altitude):
  ENU_Rotation_Matrix = np.matrix ([[ -sin(Longitude), cos(Longitude), 0],
                                    [ -cos(Longitude)*sin(Latitude), -sin(Longitude)*sin(Latitude), cos(Latitude)], 
                                    [ cos(Longitude)*cos(Latitude), sin(Longitude)*cos(Latitude), sin(Latitude)]])

  Coordinates_ECEF = np.matrix ([[ X ],
                            [ Y ], 
                            [ Z ]])

  ENU_convention = ENU_Rotation_Matrix * Coordinates_ECEF

  x = ENU_convention[0][0] 
  y = ENU_convention[1][0] 
  z = ENU_convention[2][0] 
  
  return x, y, z
