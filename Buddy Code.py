#-------------------------------------------------------------------------------

# Author:       Jonathan Davis based on Matthew Sheeter's code
# Date:         10/1/2019

#-------------------------------------------------------------------------------
import random
newgame = True
locations = ("dor1","door2","door3")

def door1():
    print("You have selected door 1.")
    if choice == dragon:
        print("This room has a dragon! Oh no!")
    elif choice == treasure:
        print("You have found treasure and exit!")
    elif choice == pit:
        print("You fell into a bottomless pit!")

def door2():
    print("You have selected door 2.")
    if choice == dragon:
        print("This room has a dragon! Oh no!")
    elif choice == treasure:
        print("You have found treasure and exit!")
    elif choice == pit:
        print("You fell into a bottomless pit!")

def door3():
    print("You have selected door 3.")
    if choice == dragon:
        print("This room has a dragon! Oh no!")
    elif choice == treasure:
        print("You have found treasure and exit!")
    elif choice == pit:
        print("You fell into a bottomless pit!")

print("Hello, What is your name?")
name = imput
print("It is nice to meet you," + name + ".")
print("Are you ready to play?")
ready = False:
while ready == False:
    choice = imput().lower()
    if choice == "yes":
        ready = True
    elif choice == "no":
        print("Okau, I will wair until you are.")
        ready = False
    else:
        print("Invalid Imput")
        ready = False

while newgame == True:
    dragon = random.choice(locations).lower()
    treasure = random.choice(locations).lower()
    pit = random.choice(locations).lower()
    ("You're in a dark dumgeon and you must eascape. There
are 3 doors.")
    print("One leads to a bottomless pit.")
    print("One leds to treasure plus the exit.")
    print("The lost one leads to a dragon.")
    print("pick a door using (door1)")
    choice = Input().lower()
    door = False
    while door == False:
    if choice == "door1":
        door1()
        room = True
    elif choice == "door2":
        door2()
        room = True
    elif choice == "door3":
        door3()
        room = True
    else:
        print("Invalid Input!")
        choice = Input().lower()
    print("Would you like to play again?")
    choice = Input().lower()
    if choice == "yes":
        print("amesome!")
    elif choice == "No":
        print("Too had, see you next time")
        newgame = False
    else:
        print("Invalid Input!")
        choice = Input().lower()
