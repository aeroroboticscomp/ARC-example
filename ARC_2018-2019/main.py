import math
from algo import *
from in_out import *


def main(filename):
    waypoints = readWaypointFile(filename)
    path = determinePath(waypoints)
    print(path)
    print(waypoints)
    return path, waypoints



if __name__ == '__main__':
    main()