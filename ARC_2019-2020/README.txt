HARC Competition 2019-2020 AUTONOMOUS README

This contains a example code for the HARC competition for 2019-2020. 

MAIN
- Runs the entire script. Reads in the waypoint file

ALGO
- takes in the waypoints and determines the order to fly the waypoints. In example code, the waypoints are shuffled randomly using a random number generator.

IN_OUT
- parses the waypoint file

WAYPOINT_1, _2, _3
- example waypoint list. All waypoint files will be in the following format: X latitude, Y latitude, altitude (ft), and Task (A,B,H)
	- Task A: Loiter (hold for 10 seconds)
	- Task B: Delivery (deliver golf ball)
	- Task H: Home (starting location)
- assume that you need to return to the home waypoint

The waypoint list file will exactly like the example file.

NOTE: GPS accuracy is very dependent on location. Judges will approve loiter waypoint execution if it is apparent that drone is hovering in the vicinity of the assigned waypoint. Teams are STRONGLY ENCOURAGED to devise other methods to improve the accuracy of autonomous drop.



