# Coordinate System Transformation 
# Transforming the system from Latitude, Longitude and Altitude (LLA) to Earth-Centred, Earth-Fixed (ECEF)

from math import sin, cos, sqrt

def LLA_2_ECEF (Latitude, Longitude, Altitude):
  a = 6378137                         # Semi-major Axis
  b = 6356752.314245                  # Semi-minor Axis
  f = (a-b)/a                         # Inverse Flattening
  e = sqrt((a**2-b**2)/a**2)          # First Eccentricity
  e2 = f*(2-f)                        # First Eccentricity Squared

  X = ((a/(sqrt(1-e2*(sin(Latitude))**2)))+Altitude)*cos(Latitude)*cos(Longitude)
  Y = ((a/(sqrt(1-e2*(sin(Latitude))**2)))+Altitude)*cos(Latitude)*sin(Longitude)
  Z = (b/a)**2*((a/sqrt(1-e2*(sin(Latitude))**2)))+Altitude)*sin(Latitude) 

return X, Y, Z

