import math
from algo import *
from in_out import *

def main(filename):
    
    # Read in waypoints
    waypoints = readWaypointFile(filename)

    # Determine path
    path = determinePath(waypoints)

    # Export path






if __name__ == '__main__':
    main()