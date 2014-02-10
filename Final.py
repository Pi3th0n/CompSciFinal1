#!/usr/bin/env python3
#
#   Authors: Chase Mansell & Stephen Simmons
#   Created: Jan 17 2014
#   Last Modified: Jan 23 2014
#   About: This is our final project for CS402. We were inspired by  #   the old game "Oregon Trail"
#
#   This is helpful: http://anydice.com/

# import ships
import random
import math

### The space below this line should be where we define all of our functions ###

# Keep track of the date
def numToDate(num):
    if num in range(1, 31):
        return ("January " + numEnding(num))
    if num in range(32, 59):
        return ("February " + numEnding(num-31))
    if num in range(60, 90):
        return ("March " + numEnding(num-59))
    if num in range(81, 120):
        return ("April " + numEnding(num-90))
    if num in range(111, 151):
        return ("May " + numEnding(num-120))
    if num in range(142, 181):
        return ("June " + numEnding(num-151))
    if num in range(172, 212):
        return ("July " + numEnding(num-181))
    if num in range(213, 243):
        return ("August " + numEnding(num-212))
    if num in range(244, 273):
        return ("September " + numEnding(num-243))
    if num in range(274, 304):
        return ("October " + numEnding(num-273))
    if num in range(305, 334):
        return ("November " + numEnding(num-304))
    if num in range(335, 365):
        return ("December " + numEnding(num-334))
    return "Error: Number not in range"


# make the grammar work
def numEnding(num):
    if str(num)[-1] == "1":
        return (str(num) + "st")
    if str(num)[-1] == "2":
        return (str(num) + "nd")
    if str(num)[-1] == "3":
        return (str(num) + "rd")
    return (str(num) + "th")
    

# Sail to a different town
def sailAway(location):
    print("You have chosen to sail to a different town")
    destination = 0
    while not destination:
        destination = input("Please enter the name of the town you would like to sail to: ")
        if destination == location:
                print("You open your mouth to give orders, then it hits you. You’re already there.")
                destination = 0
        elif destination in townlist:
                location = destination
                print("You have spent {0} days sailing to {1}.".format(4, destination))
        else:
                print("Please enter a valid destination.  Valid destinations include: ", (townlist - location))
                destination = 0


# Plunder Enemy Ships
def plunder():
    print("You will sail to sea and spend the day trying to get booty.")
    fight = random.randint(1, 5)
#Must set up the random number for each ship, with the larger ships #getting a bigger role on the dice
#Then that random role must combat your random role, which will be #relevant only if supplies are plentiful
#Can only fight if ammunition >= 20, from 4 to 15 shots per volley, #depends on each ship
#
#  if fight == 1:


### This space should be used to define our variables ###
            
PlFName = 0
PlLName = 0
difficulty = 0
1
morale = 75
money = 2500
loan = 5000
# cargo = [Food(0), Rum(1), Oranges(2), Sugar(3), Wood(4), Cloth(5), Metal(6), Cannonballs(7)]
cargo = [0, 0, 0, 0, 0, 0, 0, 0]
townlist = ["Tortuga", "Port Royal", "Havana", "Nassau", "Kingston"]
location = 0
day = 0
schooner = 1
brig = 2
frigate = 3
galleon = 4
shipOfTheLine = 5
shipspecs = {}
schoonerspecs = {"cargoSpace": 5000, "crewSize": 10, "price": 800}
brigspecs = {"cargoSpace": 12000, "crewSize": 25, "price":1200}
frigatespecs = {"cargoSpace": 22000, "crewSize": 60, "price":1600}
galleonspecs = {"cargoSpace": 32000, "crewSize": 100, "price":2200}
shipOfTheLinespecs = {"cargoSpace": 40000, "crewSize": 200, "price":2800}


### The space below this line is where the game code goes ###


# introduction
# Choose difficulty, then perform basic setup based on difficulty
while not difficulty:
    try:
            attempt = int(input("Please choose a difficulty level: 1 (easy), 2 (normal), or 3 (hard): "))
    except ValueError:
            print("The difficulty must be in the form of an integer, either 1, 2, or 3.")
    if attempt in [1, 2, 3]:
            difficulty = attempt
    else:
            print("Sorry, {0} is not a valid difficulty level".format(attempt))
morale -= 10 * difficulty
money -= 250 * difficulty
loan += 1000 * difficulty
maxdays = 100 - (15 * difficulty)
location = townlist[random.randint(0,len(townlist)-1)]
for stuff in range(len(cargo)):
    if stuff != 2 and stuff != 3:
        cargo[stuff] = 200 - (50 * difficulty)

# Now the game actually begins    
print("""    You’ve spent the past couple months sailing across the
Atlantic Ocean. You and your crew are tired but happy to finally 
walk on solid ground again.  You arrived in {0} 

""")
while not PlFName:
    PlFName = str(input("What is your first name? "))
while not PlLName:
    PlLName = str(input("What is your last name? "))

print("""Initial values:
First Name: {0}, Last Name: {1}, Difficulty: {2}, Crew Morale: {3}, Current Money: {4}, Loan: {5}, Location: {6}, Cargo: {7}""".format( PlFName, PlLName, difficulty, morale, money, loan, location, cargo))
print("It is your first day at your new job.")

while day <= maxdays:
    action = 0
    while not action:
        try:
            nextaction = int(input("""What would you like to do today?
Explore the town!------------1    
Sail to a new town!----------2
Plunder nearby enemy ships!--3
Return to England------------4
Quit-------------------------5
"""))
        except ValueError:
            print("Please enter one of the following integers: 1, 2, 3, 4, or 5.")
            nextaction = 0
        if nextaction in [1, 2, 3, 4, 5]:
            action = nextaction
        else:
            print("Please enter one of the following integers: 1, 2, 3, 4, or 5.")
            nextaction = 0
    while action == 1:
        print("You have chosen to explore the town. You have four options as to what you want to do to waste your time.")
# Places you can visit:
#    Taverns - gather information, recruit crewmembers
#    Shops - buy and sell goods
#    
#    If we have extra time - each town should have something unique
     
        while not objective:
            try:
                objective = int(input("""Where would you like to go?
The Local Tavern-------1
Shop for supplies------2
Sell goods-------------3
Quit-------------------4
"""))
            except ValueError:
                print("Please enter one of the following integers: 1, 2, 3, or 4")
            if not objective in [1, 2, 3, 4]:
                print("Please enter one of the following integers: 1, 2, 3, or 4")
                objective = 0

        if objective == 1:
            print("You will be going to the tavern today. The morale of your crew will automatically be boosted.")
#        recruit = 0
#        while not recruit:
#            recruit = input("Would you like to try and recruit some #more crew today (Yes or No): ")
#        except valueError
#        if (recruit.lower())[0] == y:
                         
        if objective == 2:
            pass
        if objective == 3:
            pass
        if objective == 4:
            pass

        
