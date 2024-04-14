# LLA to ECEF

from math import sin, cos, sqrt


Latitude = float(input('Enter the Latitude of Location (Radians): \n'))
Longitude = float(input('Enter the Longitude of Location (Radians): \n'))
Altitude = float(input('Enter the Altitude of Location (Meters): \n'))

a = 6378137                         # Semi-major Axis
b = 6356752.314245                  # Semi-minor Axis
f = (a-b)/a                         # Inverse Flattening
e = sqrt((a**2-b**2)/a**2)          # First Eccentricity
e2 = f*(2-f)                        # First Eccentricity Squared

R = a/sqrt(1-(e2*(sin(Latitude)**2)))    # Radius of Curvature in the Prime Vertical
X = (R+Altitude)*cos(Latitude)*cos(Longitude)
Y = (R+Altitude)*cos(Latitude)*sin(Longitude)
Z = ((1-e2)*R+Altitude)*sin(Latitude)

print ('Radius of Curvature: ', R)
print ('X-Coordinate:', X)
print ('Y-Coordinate:', Y)
print ('Z-Coordinate:', Z)
