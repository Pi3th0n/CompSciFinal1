#!/usr/bin/env python3
#
#   Authors: Chase Mansell & Stephen Simmons
#   Created: Jan 17 2014
#   Last Modified: Jan 23 2014
#   About: This is our final project for CS402. We were inspired by the old game "Oregon Trail"
#


#  The space above this line should be where we define all of our functions
#  This space below this line is where our game code will go

location = 0
# This variable will keep track of where in our program the player is, and should prevent the 
# program from running code that we don't want to run.

while location == 0:
    print("This is our introduction")
    PlFName = str(input("What is your first name? "))
    PlLName = str(input("What is your last name? "))
    location = 1
