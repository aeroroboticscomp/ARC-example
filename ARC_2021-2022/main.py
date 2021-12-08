import math
from algo import *
from in_out import *


def main(filename):

    # Read in waypoints
    waypoints = readWaypointFile(filename)

    # Determine path
    path = determinePath(waypoints)

    # Export path
    for i in path:  # Print out order of Lat Long
    	print("Latitude: "+str(waypoints['latitude'][i])
    	      + " Longitude: "+str(waypoints['longitude'][i]))


#donato
if __name__ == '__main__':
	main("waypoint_1.txt")
