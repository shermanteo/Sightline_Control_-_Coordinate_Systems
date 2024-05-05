# Direction Cosine Matrix (DCM)
# Rotation of the NED Coordinates to the take into account the rotation of the platform
# The rotation matrix will consist of the Roll, Pitch, Yaw matrices
# The input angles are the Yaw, Pitch and Roll angles given as (psi, theta, omega) respectively
# x, y, z are the coordinates input in NED
# Output will be x, y, z which are the NED coordinates after taking the platform rotation into consideration 

# Note: THIS CASE IS STRICTLY FOR YAW -> PITCH -> ROLL rotations only. 
# If rotations are in a different order, change the matrix multiplication around to suit the situation

import numpy as np
from math import sin, cos

def ECEF_2_NED(x, y, z, psi, theta, omega):
  Roll_Matrix = np.matrix ([[ 1, 0, 0],
                            [ 0, cos(omega), -sin(omega)], 
                            [ 0, sin(omega), cos(omega)]])
  Pitch_Matrix = np. matrix ([[ cos(theta), 0, sin(theta)],
                              [ 0, 1, 0], 
                              [ -sin(theta), 0, cos(theta)]])
  Yaw_Matrix = np. matrix ([[ cos(psi), -sin(psi), 0],
                            [ sin(psi), cos(psi), 0],
                            [ 0, 0, 1]])
  Platform_Rotation = Yaw_Matrix * Pitch_Matrix * Roll_Matrix

  NED_Matrix = np.matrix ([[ x ],
                           [ y ], 
                           [ z ]])

  Coordinates_After_Platform_Rotation = Platform_Rotation * NED_Matrix
  
  return Coordinates_After_Platform_Rotation
