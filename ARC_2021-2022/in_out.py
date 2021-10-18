import os
import sys

def readWaypointFile(filename):

	# Returns dictionary of waypoint information
    waypointFileArray = open(filename).read().split()

    # Waypoint dictionary
    waypointDict = {}
    latitude = []
    longitude = []
    latitudeDirection = []
    longitudeDirection = []
    altitude = []
    waypointType = []

    # Waypoint iteration
    for i in range(int(len(waypointFileArray)/6.0)):
        latitude.append(waypointFileArray[(i-1)*6])
        longitude.append(waypointFileArray[(i-1)*6+2])
        latitudeDirection.append(str(waypointFileArray[(i-1)*6+1]))
        longitudeDirection.append(str(waypointFileArray[(i-1)*6+3]))
        altitude.append(waypointFileArray[(i-1)*6+4])
        waypointType.append(str(waypointFileArray[(i-1)*6+5]))

    waypointDict['latitude'] = latitude
    waypointDict['longitude'] = longitude
    waypointDict['longitudeDirection'] = longitudeDirection
    waypointDict['latitudeDirection'] = latitudeDirection
    waypointDict['altitude'] = altitude
    waypointDict['waypointType'] = waypointType

    return waypointDict

