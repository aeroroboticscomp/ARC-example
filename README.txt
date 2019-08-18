HARC Competition 2019-2020 AUTONOMOUS README

This contains a example code for the HARC competition for 2017-2018. Note, this only runs the "separate" determination. The files do the following:

MAIN
- Runs the entire script. Reads in the waypoint file

ALGO
- takes in the waypoints and determines the order to fly the waypoints. In example code, the waypoints are shuffled randomly using a random number generator.

IN_OUT
- parses the waypoint file

WAYPOINT_1, _2, _3
- example waypoint list. All waypoint files will be in the following format: X latitude, Y latitude, and Task (A,B,H)
	- Task A: Loiter
	- Task B: Delivery
	- Task H: Home
- assume that you need to return to the home waypoint



