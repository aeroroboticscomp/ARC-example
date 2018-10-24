from dronekit import connect, VehicleMode, LocationGlobalRelative
# from Waypoint import main
import time
import main

#===========================================
# Predefined Functions
#===========================================

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to a TargetAltitude.
    """

    print "Basic pre-arm checks"
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print "Reached target altitude"
            break
        time.sleep(1)


#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None



#================================================
# Connection or SITL
#================================================

#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)


#================================================
# Route Determination
#================================================

# Read in waypoints and determine route

path, waypoints = main.main("waypoint_1.txt")

#===========================================================
# Flight Procedure
#===========================================================

# Arm and takeoff
arm_and_takeoff(10) # 10 m

# Set default speed to 3 m/s
vehicle.airspeed = 3

# Go through each waypoint
for point in path:

    # if Loiter
    if waypoints['waypointType'][point] == 'A':
        print "Initiating Loiter Waypoint"
        point1 = LocationGlobalRelative(float(waypoints['latitude'][point]), float(waypoints['longitude'][point]), float(waypoints['altitude'][point]))
        vehicle.simple_goto(point1)
        time.sleep(30) # Set at 30 seconds, could do better in trying to predict time to location

    # if delivery
    if waypoints['waypointType'][point] == 'B':
        print "Initiating Delivery Waypoint"
        point1 = LocationGlobalRelative(float(waypoints['latitude'][point]), float(waypoints['longitude'][point]), float(waypoints['altitude'][point]))
        vehicle.simple_goto(point1)
        time.sleep(30) # Set at 30 seconds, could do better in trying to predict time to location
        # Deliver Payload
        print "Delivering Payload"
        vehicle.channels.overrides = {'6': 300}
        print " Channel overrides: %s" % vehicle.channels.overrides
        print "Payload Delivered!!"


# Once gone through each waypoint, return to launch
print "Land"
vehicle.mode = VehicleMode("LAND")
# Give it time for it to fully land
time.sleep(30)

#============================
# Close up
#============================

# Disarm
print "Disarm Vehicle"
vehicle.armed = False
# Confirm vehicle armed before attempting to take off
while vehicle.armed:
    print " Waiting for disarming..."
    time.sleep(1)

# Close vehicle object before exiting script
print "Close vehicle object"
vehicle.close()

# Shut down simulator if it was started.
if sitl is not None:
    sitl.stop()