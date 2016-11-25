# import statements
from Menu import *
# from Game import Game

# variables 
active = 1
usrChoice = 0
prompt = '==>> '

def playGame(num):
    
    print "you chose to play game %d" % (num)
    print "unfortunately, this game isn't ready."
    print "please press enter to return to the main menu."
    raw_input()

# this while loop runs the full program until the program quits
while active == 1:

    # show the menu TODO something
    menu = Menu()
    usrChoice = menu.showMenu(prompt)
    
    # execute the choice
    if usrChoice > 0:
        playGame(usrChoice)
    elif usrChoice == 0:
        active = 0
    else:
        print "We don't recognize that choice, please try again."
        print "Press enter to make another choice."
        raw_input(prompt)

    # loop back around