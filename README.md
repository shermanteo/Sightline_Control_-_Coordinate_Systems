# Coordinate_Systems

## Project Overview
There are several coordinate systems that are being used around the world which may confuse us at times. These coodrinate systems may be trivial to some however for others, it proves to be of utmost importance especially when it involves interpreting one coordinate system and how it applies to the other. For example, there are maps which give the Latitude, Longitude and Altitude however, it is not as intuitive when we need to calculate much smaller differences in displacements hence preferring to use X, Y and Z instead. There are a variety of different coordinate systems and each has their benefits and detriments however, this project will cover just the transformation of between coordinate systems. 

All constants used are in accordance to WGS84.

## Brief Overview of Coordinate Systems
- Geodetic Coordinate System



- Geocentric Coordinate System/Earth-Centered, Earth-Fixed (ECEF) Coordinate System:
A three-dimensional, earth-centered reference system in which locations are identified by their x-, y-, and z-values. The x-axis is in the equatorial plane and intersects the prime meridian (usually Greenwich). The y-axis is also in the equatorial plane; it lies at right angles to the x-axis and intersects the 90-degree meridian. The z-axis coincides with the polar axis and is positive toward the north pole. The origin is located at the center of the sphere or spheroid.


- Local Vertical Coordinate System: 



- North-East-Down (NED) Convention and East-North-Up (ENU) Convention:
There are two main ways to display our coordinate systems mainly NED or ENU convention. This is especially important when working with different frames of references such as aircrafts, sea vehicles and land vehicles. Different scenarios will utilise different conventions depending on the platforms requirements and how the user wishes to use and display the information. 

  Coordinates to describe an aircraft attitude (Heading, Elevation and Bank) are       normally given relative to a reference control frame located in a control tower, and therefore ENU, relative to the position of the control tower on the earth surface.

  Coordinates to describe observations made from an aircraft are normally given relative to its intrinsic axes, but normally using as positive the coordinate pointing downwards, where the interesting points are located. Therefore, they are normally NED.


## Geodetic Coordinate System to Geocentric Coordinate System
For the Geodetic Coordinate System, 
- Geodetic Latitude: Measured in the plane of the local meridian from the Earth's true Equator to the geodetic local vertical, measured positive north from the Equator.
- Geodetic Longitude: Measured in the plane of the Earth's true Equator from the Greenwich meridian to the local meridian, measured positive eastward.
- Geodetic Altitude: The distance from the selected point to the reference geoid, measured along the geodetic local vertical, and is positive for points outside the geoid.

For the Geocentric Coordinate System, it uses a cartesian coordinate system hence it would be more intuitive for others to understand especially for those who are familiar with matrices. Hence, there are reasons as to why individuals would prefer to work in the Geocentric Coordinate System as compared to Geodetic. 

## Geocentric Coordinate System to Local Vertical Coordinate System (ENU Convention)


## Geocentric Coordinate System to Local Vertical Coordinate System (NED Convention)


## Acknowledgment, Credits and Suggested Readings
All the knowledge and concepts which were being used in this project should be credited to the authors of the sites, papers and books:

https://science-data.larc.nasa.gov/LITE/level1doc/geodetic_coords.html
https://docs.oracle.com/cd/A91202_01/901_doc/appdev.901/a88805/sdo_cs_c.htm
https://en.wikipedia.org/wiki/Axes_conventions
