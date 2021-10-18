HARC Competition 2021-2022 AUTONOMOUS README

This contains a example code for the ARC competition for 2021-2022. 

MAIN
- Runs the entire script. Reads in the waypoint file

ALGO
- takes in the waypoints and determines the order to fly the waypoints. In example code, the waypoints are shuffled randomly using a random number generator.

IN_OUT
- parses the waypoint file

WAYPOINT_1, _2, _3
- example waypoint list. All waypoint files will be in the following format: X latitude, Y latitude, altitude (ft), and Task (A,B,H). Please see the rulebook for the details about the specific tasking being asked at each waypoint.
	- Task A: Loiter 
	- Task B: Surveilance Waypoint 1 
	- Task C: Surveilance Waypoint 2 
	- Task H: Home (starting location)
- You need to return to the home waypoint (i.e. a complete flight is home, waypoint 1, waypoint 2, waypoint 3, waypoint 4, home).

The competition waypoint list file will look exactly like the example file.

NOTE: GPS accuracy is very dependent on location. Judges will approve loiter waypoint execution if it is apparent that drone is hovering in the vicinity of the assigned waypoint. Teams are STRONGLY ENCOURAGED to devise other methods besides flying to improve the accuracy of autonomous drop. Teams can add additional equipment to their drones as long as it does not compromise the air-worthiness of the drone.



