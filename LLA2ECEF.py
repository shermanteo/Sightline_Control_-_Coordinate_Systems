# LLA to ECEF

from math import sin, cos, sqrt


Phi = float(input('Enter the Latitude of Location (Radians): \n'))
Lambda = float(input('Enter the Longitude of Location (Radians): \n'))
H = float(input('Enter the Altitude of Location (Meters): \n'))

a = 6378137                         # Semi-major Axis
b = 6356752.314245                  # Semi-minor Axis
f = (a-b)/a                         # Inverse Flattening
e = sqrt((a**2-b**2)/a**2)          # First Eccentricity
e2 = f*(2-f)                        # First Eccentricity Squared

R = a/sqrt(1-(e2*(sin(Phi)**2)))    # Radius of Curvature in the Prime Vertical
X = (R+H)*cos(Phi)*cos(Lambda)
Y = (R+H)*cos(Phi)*sin(Lambda)
Z = ((1-e2)*R+H)*sin(Phi)

print ('Radius of Curvature: ', R)
print ('X-Coordinate:', X)
print ('Y-Coordinate:', Y)
print ('Z-Coordinate:', Z)