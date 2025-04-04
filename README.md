# Sightline Control and Coordinate Systems Transformations
 
## Project Overview
There are several coordinate systems that are being used around the world which may confuse us at times. These coordinate systems may be trivial to some however for others, it proves to be of utmost importance especially when it involves interpreting one coordinate system and how it applies to the other. For example, there are maps which give the Latitude, Longitude and Altitude however, it is not as intuitive when we need to calculate much smaller differences in displacements hence preferring to use X, Y and Z instead. There are a variety of different coordinate systems and each has their benefits and detriments however, this project will cover just the transformation of between coordinate systems and subsequently using all these knowledge to create a code for sightline control. 

All constants used are in accordance to WGS84.

# Brief Overview of Sightline Control
Sightline control refers to the management and regulation of visual lines of sight within a given space, often in urban planning, architecture, or scenic conservation. It involves ensuring that specific views or vistas are protected, enhanced, or regulated to achieve desired aesthetic, functional, or regulatory goals.

## Key aspects of sightline control include:
- Protection of Views: Sightline control aims to safeguard significant or iconic views from obstruction or degradation. This can involve zoning regulations, design guidelines, or legal protections to preserve sightlines to landmarks, natural features, or cultural heritage sites.
- Visual Impact Assessment: Before undertaking development projects, especially those in sensitive areas, sightline assessments may be conducted to evaluate potential visual impacts. This involves analyzing how proposed changes to the landscape or built environment might affect existing views and vistas.
- Design Integration: In urban design and architecture, sightline control is often integrated into the design process to optimize visual connections and perspectives. Designers may strategically orient buildings, public spaces, or infrastructure to frame or enhance specific views, creating memorable experiences for inhabitants and visitors.
- Vegetation Management: Vegetation, such as trees and shrubs, can significantly influence sightlines. Sightline control may involve vegetation management strategies to preserve or enhance views, such as selective pruning, strategic planting, or tree preservation ordinances.
- Regulatory Tools: Municipalities may implement zoning ordinances, land use regulations, or design guidelines to enforce sightline control objectives. These regulations can stipulate building height limits, setbacks, view corridors, or other measures to protect or enhance important views.

Overall, sightline control plays a vital role in shaping the visual character and quality of urban and natural landscapes, ensuring that views of significance are respected, maintained, or enhanced for the benefit of communities and the environment.

# Brief Overview of Coordinate Systems
## Geodetic Coordinate System
The geodetic coordinate system is a three-dimensional coordinate system used to specify the position of points on the surface of the Earth. It consists of latitude, longitude, and altitude (or elevation).

Latitude measures how far north or south a point is from the Equator, ranging from 0° at the Equator to 90°N at the North Pole and 90°S at the South Pole. Longitude measures the east-west position of a point relative to the Prime Meridian, which runs through Greenwich, England, with values ranging from 0° to 180°E and 0° to 180°W. Altitude, also known as elevation, represents the height of a point above or below a reference surface, such as sea level.

Together, latitude and longitude provide a way to pinpoint any location on Earth's surface, while altitude adds the third dimension, making it possible to specify the height of a point relative to a reference surface. This coordinate system is fundamental for various applications, including navigation, surveying, cartography, and GIS (Geographic Information Systems).

## Geocentric Coordinate System/Earth-Centered, Earth-Fixed (ECEF) Coordinate System:
The geocentric coordinate system is a three-dimensional coordinate system centered at the center of the Earth, also known as the geocenter. Unlike the geodetic coordinate system, which is based on the Earth's surface, the geocentric system treats the Earth as a perfect sphere or an ellipsoid and specifies positions relative to its center.

In this system, three coordinates are used to describe a point: geocentric latitude, longitude, and radial distance. Geocentric latitude measures the angle between the equatorial plane and a line connecting the point to the Earth's center, ranging from 0° at the equator to 90° at the poles. Longitude measures the angle between a reference meridian and the meridian passing through the point, similar to the geodetic system. Radial distance represents the straight-line distance from the point to the Earth's center.

The geocentric coordinate system is commonly used in astronomy, satellite tracking, and geodesy, where precise positioning relative to the Earth's center is required. It provides a consistent reference frame for global measurements and calculations, essential for activities such as satellite orbit determination, Earth rotation studies, and geophysical modeling.


## Local Vertical Coordinate System: 
The local coordinate system is a Cartesian coordinate system established within a defined local area, providing a frame of reference relative to a specific point or object of interest. Unlike global coordinate systems such as geodetic or geocentric systems, which cover the entire Earth, the local coordinate system is localized and typically used for smaller areas or projects.

The local coordinate system typically has three orthogonal axes, often denoted as:

X-axis: Usually aligned with a chosen direction within the local area, representing the east-west direction.
Y-axis: Perpendicular to the X-axis, representing the north-south direction.
Z-axis: Represents the vertical dimension, typically aligned with the local gravitational direction or a predefined vertical reference.
The origin of the local coordinate system is usually set at a specific point within the local area, such as the starting point of a construction project or the centroid of a surveyed region.

Local coordinate systems are widely used in engineering, construction, urban planning, GIS (Geographic Information Systems), and other fields where precise local positioning and spatial referencing are required. They provide a convenient and practical way to express locations, distances, and orientations within a localized context, facilitating design, analysis, and decision-making processes.


## North-East-Down (NED) Convention:
The NED (North-East-Down) coordinate system is a local, Cartesian coordinate system commonly used in aviation, robotics, and other fields where a local frame of reference is needed. In the NED system, three orthogonal axes are defined:

North (N): Points in the direction of increasing latitude.
East (E): Points in the direction of increasing longitude.
Down (D): Points opposite to the direction of gravity.
The origin of the NED coordinate system is typically set at a specific point of interest, such as an aircraft's starting position or a robotic vehicle's initial location.

This system provides a convenient way to express positions and orientations relative to a local reference point, making it useful for navigation, control, and localization tasks. By using NED coordinates, movements and orientations can be described in a simple and intuitive manner, facilitating various engineering applications.

## East-North-Up (ENU) Convention:
The ENU (East-North-Up) coordinate system is a local, Cartesian coordinate system commonly used in navigation, geodesy, and robotics. In the ENU system, three orthogonal axes are defined:

East (E): Points in the direction of increasing longitude.
North (N): Points in the direction of increasing latitude.
Up (U): Points in the direction of increasing altitude or elevation.
The origin of the ENU coordinate system is typically set at a specific point of interest, such as a reference point or the starting location of a vehicle.

This system provides a convenient way to express positions and orientations relative to a local reference point, making it useful for navigation, mapping, and control tasks. By using ENU coordinates, movements and orientations can be described in a straightforward and intuitive manner, facilitating various engineering and scientific applications.


## Acknowledgment, Credits and Suggested Readings
All the knowledge and concepts which were being used in this project should be credited to the authors of the sites, papers and books:

https://apps.dtic.mil/sti/pdfs/ADA484864.pdf
https://science-data.larc.nasa.gov/LITE/level1doc/geodetic_coords.html
https://docs.oracle.com/cd/A91202_01/901_doc/appdev.901/a88805/sdo_cs_c.htm
https://en.wikipedia.org/wiki/Axes_conventions
https://www.suncam.com/miva/downloads/docs/360.pdf
https://www.suncam.com/miva/downloads/docs/359.pdf
https://www.suncam.com/miva/downloads/docs/358.pdf
