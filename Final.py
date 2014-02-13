#!/usr/bin/env python3
#
# Authors: Chase Mansell & Stephen Simmons
# Created: Jan 17 2014
# Last Modified: Jan 23 2014
# About: This is our final project for CS402. We were inspired by # the old game "Oregon Trail"
#
# This is helpful: http://anydice.com/

# import ships
import random
import math

### The space below this line should be where we define all of our functions ###

# Keep track of the date
def numToDate(num):
    if num in range(1, 32):
        return ("January " + numEnding(num))
    if num in range(32, 60):
        return ("February " + numEnding(num-31))
    if num in range(60, 91):
        return ("March " + numEnding(num-59))
    if num in range(81, 121):
        return ("April " + numEnding(num-90))
    if num in range(111, 152):
        return ("May " + numEnding(num-120))
    if num in range(142, 182):
        return ("June " + numEnding(num-151))
    if num in range(172, 213):
        return ("July " + numEnding(num-181))
    if num in range(213, 244):
        return ("August " + numEnding(num-212))
    if num in range(244, 274):
        return ("September " + numEnding(num-243))
    if num in range(274, 305):
        return ("October " + numEnding(num-273))
    if num in range(305, 335):
        return ("November " + numEnding(num-304))
    if num in range(335, 366):
        return ("December " + numEnding(num-334))
    return "Error: Number not in range"

# Because we ask a lot of yes or no questions
def yesOrNo():
    a = ""
    while a == "":
        a = input("Yes/No? ")
        if (a.lower())[0] == "y":
            return True
        elif (a.lower())[0] == "n":
            return False
        else:
            print("You're a stupid fuck. Try yes or no.")
            a = ""

# make the grammar work
def numEnding(num):
    if str(num)[-1] == "1":
        if (len(str(num)) >= 2 and str(num)[-2] != "1") or len(str(num)) < 2:
            return (str(num) + "st")
    if str(num)[-1] == "2":
        if (len(str(num)) >= 2 and str(num)[-2] != "1") or len(str(num)) < 2:
            return (str(num) + "nd")
    if str(num)[-1] == "3":
        if (len(str(num)) >= 2 and str(num)[-2] != "1") or len(str(num)) < 2:
            return (str(num) + "rd")
    return (str(num) + "th")

# Plunder Enemy Ships
def plunder():
    print("You will sail to sea and spend the day trying to get booty.")
    fight = random.randint(1, 5)
#Must set up the random number for each ship, with the larger ships #getting a bigger role on the dice
#Then that random role must combat your random role, which will be #relevant only if supplies are plentiful
#Can only fight if ammunition >= 20, from 4 to 15 shots per volley, #depends on each ship
#
# if fight == 1:


### This space should be used to define our variables ###
            
PlFName = 0
PlLName = 0
difficulty = 0
morale = 75
money = 2500
loan = 5000
# cargo = [Food(0), Rum(1), Oranges(2), Sugar(3), Cannonballs(4)]
cargo = [0, 0, 0, 0, 0]
townlist = ["Tortuga", "Port Royal", "Havana", "Nassau", "Kingston"]
foodPrices = {"Tortuga":1, "Port Royal":2, "Havana": 3, "Nassau":4, "Kingston":5}
rumPrices = {"Tortuga":1, "Port Royal":2, "Havana": 3, "Nassau":4, "Kingston":5}
ballPrices = {"Tortuga":1, "Port Royal":2, "Havana": 3, "Nassau":4, "Kingston":5}
location = 0
day = 0
atSea = False
sailCount = 0
fightMax = 4 - difficulty
fightCount = 0
whichShip = {1: "schooner", 2: "brig", 3: "frigate", 4: "galleon", 5:"Ship of the Line"}
#[Ship’s HP(0), Your HP(1), # of Crew(2)]
health = [100, 10, 0]
shipspecs = {}
schoonerspecs = {"cargoSpace": 5000, "crewSize": 10, "price": 800, "power": 1, "maxHealth": 100, "number":1}
brigspecs = {"cargoSpace": 12000, "crewSize": 25, "price":1200, "power": 2, "maxHealth": 200, "number":2}
frigatespecs = {"cargoSpace": 22000, "crewSize": 60, "price":1600, "power": 3, "maxHealth": 300, "number":3}
galleonspecs = {"cargoSpace": 32000, "crewSize": 100, "price":2200, "power": 4, "maxHealth": 400, "number":4}
shipOfTheLinespecs = {"cargoSpace": 40000, "crewSize": 200, "price":2800, "power": 5, "maxHealth": 500, "number":5}


### The space below this line is where the game code goes ###


# introduction
# Choose difficulty, then perform basic setup based on difficulty
while not difficulty:
    try:
            difficulty = int(input("Please choose a difficulty level: 1 (easy), 2 (normal), or 3 (hard): "))
    except ValueError:
            print("The difficulty must be in the form of an integer, either 1, 2, or 3.")
    if not difficulty in [1, 2, 3]:
            print("Sorry, {0} is not a valid difficulty level".format(difficulty))
            difficulty = 0
morale -= 10 * difficulty
money -= 250 * difficulty
loan += 1000 * difficulty
maxday = 355
day = 115 + 30 * difficulty
location = townlist[random.randint(0,len(townlist)-1)]
if difficulty == 1:
    shipspecs = galleonspecs
elif difficulty == 2:
    shipspecs = frigatespecs
else:
    shipspecs = brigspecs
health[0] = shipspecs["maxHealth"]
health[2] = shipspecs["crewSize"]
for stuff in range(len(cargo)):
    if stuff != 2 and stuff != 3:
        cargo[stuff] = 500 - (100 * difficulty)

# Now the game actually begins
print("""You left England a few months ago with a privateering contract
to hunt Spanish ships in the Caribbean. You’ve spent the past couple
months sailing across the Atlantic Ocean, and this morning you finally
sighted land. As you get closer, one of your crewmembers recognizes it
as {0}, and you decide to dock and resupply after your long
journey. As your ship pulls up, the harbormaster greets you and asks
you for your name.""".format(location))
while not PlFName:
    PlFName = str(input("What is your first name? "))
while not PlLName:
    PlLName = str(input("What is your last name? "))
print("\"Greetings captain {0}, and welcome to {1}. Please, make yourself at home.\"".format(PlLName, location))
action = 0

while day <= maxday:
    print("""Today is {0}. {13}.
You current money is {1} Reales.  The amount of money you owe your
investors is {2} Reales. You are currently in {3}. You have
{4} crates of food, {5} barrels of rum, {6} crates of oranges,
{7} bags of sugar, and {8} cannonballs. Your {9} is at about
{10}% hull integrity and has {11} crewmembers onboard.
You have {12} hp. """.format(numToDate(day%365) if day%365 != 0 else 365, money, loan, location, cargo[0]/8, cargo[1]/8, cargo[2]//4, cargo[3]//4, cargo[4], whichShip[shipspecs["number"]], int(100*(health[0]/shipspecs["maxHealth"])), health[2], health[1], "You have {0} days remaining before you must sail back to england".format(maxday - day) if maxday != day else "Today you must sail back to England and repay your investors."))
    if not atSea:
        print("""What would you like to do today?
Sail to a new town!----------1
Explore the town!------------2
Plunder nearby enemy ships!--3
Return to England------------4
Quit-------------------------5
""")
    else:
        print("""You are currently sailing to {0}. You expect to arrive
in about {1} days. Plundering could help you earn money,
however it will delay your progress towards {0}.
What would you like to do today?
Keep sailing!----------------1
Plunder nearby enemy ships!--3
Return to England------------4
Quit-------------------------5
""".format(location, sailCount))
    nextaction = ""
    while not action and not atSea:
        try:
            nextaction = int(input(""))
        except ValueError:
            print("{0} is not an integer. Please enter one of the following integers: 1, 2, 3, 4, or 5.".format(nextaction))
        if nextaction in [1, 2, 3, 4, 5]:
            action = nextaction
        else:
            print("{0} is outside the range. Please enter one of the following integers: 1, 2, 3, 4, or 5.".format(nextaction))
            nextaction = 0

    while not action and atSea:
        try:
            nextaction = int(input(""))
        except ValueError:
            print("{0} is not an integer. Please enter one of the following integers: 1, 3, 4, or 5.".format(nextaction))
        if nextaction in [3, 4, 5]:
            action = nextaction
        elif nextaction == 1:
            sailCount -= 1
            action = 6
        else:
            print("{0} is outside the range. Please enter one of the following integers: 1, 3, 4, or 5.".format(nextaction))
            nextaction = 0

    while action == 1:
        print("You have decided to sail to a new town")
        destination = ""
        while destination == "":
            destination = input("Please enter the name of the town you would like to sail to: ")
            if destination == location:
                print("You open your mouth to give orders, then it hits you. You’re already there.")
            elif destination in townlist:
                location = destination
                print("You will spend the next {0} days sailing to {1}.".format(4, destination))
                atSea = True
                sailCount += 4
            else:
                print("Please enter a valid destination. Valid destinations include: ", (townlist))
                destination = ""
        action = 6

        
    while action == 2:
        print("You have chosen to explore the town. You have four options as to what you want to do to waste your time.")
        # Places you can visit:
        # Taverns - gather information, recruit crewmembers
        # Shops - buy and sell goods
        #
        # If we have extra time - each town should have something unique
     
        objective = 0
        while not objective:
            try:
                objective = int(input("""Where would you like to go?
The Local Tavern-------1
Shop for supplies------2
Sell goods-------------3
Quit-------------------4
"""))
            except ValueError:
                print("Please enter an integer.")
            if not objective in [1, 2, 3, 4]:
                print("{0} is outside the range. Please enter one of the following integers: 1, 2, 3, or 4".format(objective))
                objective = 0

        if objective == 1:
            print("You will be going to the tavern today. You will gain 5 extra crew members and boost the morale of your crew.")
                         
        if objective == 2:
            print("You go buy supplies.")
            purchase = input("""What would you like to purchase today?
Food-------------------1
Rum--------------------2
Cannonballs------------3
""")
            quantity = 0
            if purchase.lower() == "food" or purchase == "1":
                print("The price of food in {0} is {1}.".format(location, foodPrices[location]))
                purchase = 0
            elif purchase.lower() == "rum" or purchase == "2":
                print("The price of rum in {0} is {1}.".format(location, rumPrices[location]))
                purchase = 0
            elif purchase.lower() == "cannonballs" or purchase == "3":
                print("The price of cannonballs in {0} is {1}.".format(location, ballPrices[location]))
                purchase = 0
            else:
                print("Please enter what you wish to purchase (Food, Rum, Cannonballs)")
        
        if objective == 3:
            print("You go sell some of your cargo")
        if objective == 4:
            print("You decide to finish exploring the town for the day")
            action = 6

            
    while action == 3:
        print("You have decided to plunder nearby enemey ships!")
        print(("You have {0} cannonballs. Are you sure you want to fight? ").format(cargo[4]))
        if yesOrNo():
            ship = random.randint(1, 5)
            if ship == 1:
                #print(schooner)
                print("A schooner is spotted on the horizon. Would you like to fight? ")
                if yesOrNo():
                    roll = (random.randint(1, 6)) * (shipspecs["power"])
                    opponent = random.randint(1, 6)
                    if (roll - opponent) > 2:
                        print("You have won the fight and taken minimal casualties. The ship’s cargo is yours.")
                        health[2] -= 1
                        fightCount += 1
                    elif (roll - opponent) > -1:
                        print("It was a close battle, but you managed to defeat your adversary.  You have won their cargo at the price of some of your crew members")
                        health[2] -= 3
                        health[1] -= 1
                        fightCount += 1
                    else:
                        print("The enemy put up a fight bigger than you could take. You took many casualties and have lost the battle.")
                        health[2] -= shipspecs["crewSize"]//2
                        health[1] -= 5
                        action = 6
                else:
                    print("You have decided not to fight the schooner.")
                    fightCount += 1
            elif ship == 2:
                #print(brig)
                print("A brig is spotted on the horizon. Would you like to fight? ")
                if yesOrNo():
                    roll = (random.randint(1, 6)) * (shipspecs["power"])
                    opponent = (random.randint(1, 6))* 2
                    if (roll - opponent) > 2:
                        print("You have won the fight and taken minimal casualties. The ship’s cargo is yours.")
                        health[2] -= 2
                        fightcount += 1
                    elif (roll - opponent) > -1:
                        print("It was a close battle, but you managed to defeat your adversary.  You have won their cargo at the price of some of your crew members")
                        health[2] -= 5
                        health[1] -= 2
                        fightcount += 1
                    else:
                        print("The enemy put up a fight bigger than you could take. You took many casualties and have lost the battle.")
                        health[2] -= shipspecs["crewSize"]//2
                        health[1] -= 5
                        action = 6
                else:
                    print("You have decided not to fight the brig.")
                    fightCount += 1

            elif ship == 3:
                #print(frigate)
                print("A frigate is spotted on the horizon. Would you like to fight? ")
                if yesOrNo():
                    roll = (random.randint(1, 6)) * (shipspecs["power"])
                    opponent = (random.randint(1, 6))* 3
                    if (roll - opponent) > 2:
                        print("You have won the fight and taken minimal casualties. The ship’s cargo is yours.")
                        health[2] -= 3
                        fightCount += 1
                    elif (roll - opponent) > -1:
                        print("It was a close battle, but you managed to defeat your adversary.  You have won their cargo at the price of some of your crew members")
                        health[2] -= 8
                        health[1] -= 2
                        fightCount += 1
                    else:
                        print("The enemy put up a fight bigger than you could take. You took many casualties and have lost the battle.")
                        health[2] -= shipspecs["crewSize"]//2
                        health[1] -= 5
                        action = 6
                else:
                    print("You have decided not to fight the frigate.")
                    fightCount += 1

            elif ship == 4:
                #print(galleon)
                print("A galleon is spotted on the horizon. Would you like to fight? ")
                if yesOrNo():
                    roll = (random.randint(1, 6)) * (shipspecs["power"])
                    opponent = (random.randint(1, 6))* 4
                    if (roll - opponent) > 2:
                        print("You have won the fight and taken minimal casualties. The ship’s cargo is yours.")
                        health[2] -= 4
                        fightCount += 1
                    elif (roll - opponent) > -1:
                        print("It was a close battle, but you managed to defeat your adversary.  You have won their cargo at the price of some of your crew members")
                        health[2] -= 10
                        health[1] -= 3
                        fightCount += 1
                    else:
                        print("The enemy put up a fight bigger than you could take. You took many casualties and have lost the battle.")
                        health[2] -= shipspecs["crewSize"]//2
                        health[1] -= 5
                        action = 6
                else:
                    print("You have decided not to fight the galleon.")
                    fightCount += 1

            elif ship == 5:
                #print(shipOfTheLine)
                print("A Ship of the Line is spotted on the horizon. Would you like to fight? ")
                if yesOrNo():
                    roll = (random.randint(1, 6)) * (shipspecs["power"])
                    opponent = (random.randint(1, 6))* 5
                    if (roll - opponent) > 2:
                        print("You have won the fight and taken minimal casualties. The ship’s cargo is yours.")
                        health[2] -= 5
                        fightCount += 1
                    elif (roll - opponent) > -1:
                        print("It was a close battle, but you managed to defeat your adversary.  You have won their cargo at the price of some of your crew members")
                        health[2] -= 15
                        health[1] -= 4
                        fightCount += 1
                    else:
                        print("The enemy put up a fight bigger than you could take. You took many casualties and have lost the battle.")
                        health[2] -= shipspecs["crewSize"]//2
                        health[1] -= 5
                        action = 6
                else:
                    print("You have decided not to fight the Ship of the Line.")
                    fightCount += 1
                    
            print(fightCount, fightMax)
            if fightCount < fightMax:
                print("Would you like to look for another ship to fight?")
                if yesOrNo():
                    action = 3
                else:
                    action = 6
            else:
                print("You have run out of time for fighting today")
                action = 6
        else:
            print("You have decided not to fight, but you still have enough time to do something else with your day")
            action = 0
        
        
    while action == 4:
        print("You have decided to return to england!")
        if cargo[1] < 35 * health[2]:
            print("You can’t drink saltwater, jackass. If you’d brought more rum, maybe you and your crew would have made it back to England alive. (This is a bad ending)")
            action = 7
        elif cargo[0] < 35 * health[2]:
            print("You starved to death on the way back to England because you didn’t bring enough food. Well done. (Not a good ending, if I do say so myself)")
            action = 7
        elif money < loan:
            print("You return to England but do not have the funds to pay your investors off. They have reported you to the authorities and you and your crew will be spending the rest of your lives in jail. Good going Captain. (This is a bad ending, FYI) ")
            action = 7
        else:
            print(("You have made it back to England with proper amounts of supplies and the money to pay off your investors. You and your crew now have {0} reales to throw away in England. Congrats, you won! (This is the good ending) ").format((money - loan)))
            action =7    
        
        
    while action == 5:
        print("WARNING: Your game will not be saved. Are you sure you want to continue?")
        if yesOrNo():            
            action = 7
        else:
            action = 0
        
    while action == 6:
        print("Your day draws to a close.  Your crew has eaten some food onboard and drank some rum.")
        cargo[0] -= health[2]
        cargo[1] -= health[2]
        for stuff in range(len(cargo)-1):
            if cargo[stuff] < 0:
                cargo[stuff] = 0
        if sailCount <= 0:
            atSea = False
            print("You've arrived at {0}!".format(location))
        day += 1
        fightCount = 0
        action = 0

        
    if action == 7:
        break

