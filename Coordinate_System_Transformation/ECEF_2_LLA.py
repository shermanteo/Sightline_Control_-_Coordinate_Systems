# Coordinate System Transformation 
# Transforming the system from Earth-Centred, Earth-Fixed (ECEF) to Latitude, Longitude and Altitude (LLA)

from math import sin, cos, sqrt, atan2

def ECEF_2_LLA (X, Y, Z):
  a = 6378137                         # Semi-major Axis
  b = 6356752.314245                  # Semi-minor Axis
  f = (a-b)/a                         # Inverse Flattening
  e = sqrt((a**2-b**2)/a**2)          # First Eccentricity
  e2 = f*(2-f)                        # First Eccentricity Squared
  s = sqrt(X**2 + Y**2)

  
  longitude = atan2(Y, X)
  initial_guess_reduced_latitude = atan2(Z, (1-f)*s)
  initial_guess_latitude = atan2(Z+((e2*(1-f))/(1-e2))*a*(sin(initial_guess_reduced_latitude))**3, s-e2*a*(cos(initial_guess_reduced_latitudee))**3)

  reduced_latitude = atan2((1-f)*sin(initial_guess_latitude), cos(initial_guess_latitude))
  latitude = atan2(Z+((e2*(1-f))/(1-e2))*a*(sin(reduced_latitude))**3, s-e2*a*(cos(reduced_latitudee))**3)
  
  N = (a/sqrt(1-e2*(sin(latitude))**2))
  altitude = s*cos(latitude) + (Z+e2*N*sin(latitude))*sin(latitude) - N

return latitude, longitude, altitude
