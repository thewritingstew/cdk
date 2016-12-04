# import statements
from Menu import *
from Engine import *
# from Game import Game


def playGame(num):

    print "you chose to play game %d" % (num)
    print "unfortunately, this game isn't ready."
    print "please press enter to return to the main menu."
    raw_input()

def chooseOption(menuToCheck):
    # try checks that person entered an int
    try:
        usrChoice = int(raw_input(prompt))
        # check that int is valid
        valid = menuToCheck.checkValid(usrChoice) # process the choice with Menu()
        
    except ValueError:
        # if int() errors out, then set the validity to 0
        valid = 0

    # process usrChoice based on whether it is valid or not
    if valid == 1:
        # if usrChoice is 0, then return zero (to quit game)
        if usrChoice == 0:
            return 0
        else:
            ## TODO 
            # add functionality to decipher which engine to call. Right now 
            # only calling the gameEngine, but eventually we'll want to move
            # the quit selection to the mainEngine or whatever we call it.
            ## END TODO
            # call the object that holds the correct section and send it the choice
            gameEngine.useChoice(usrChoice) # TODO build useChoice()
            return 1
    else:
        # call invalid selection
        menuToCheck.badChoice()
        menuToCheck.showMenu()
        return 1

def gameRunner(active):
    # this while loop runs the full program until the program quits
    while active == 1:

        # show the menu
        menu1 = Menu(gameEngine.menuList)
        menu1.showMenu()

        # call the chooseOption() function
        active = chooseOption(menu1)

        # END WHILE LOOP

if __name__ == "__main__":
    # variables
    active = 1
    usrChoice = 'invalid' # holds user input for menu
    prompt = '==>> '

    # create an engine, which will create games
    gameEngine = Engine('default')
#    mainEngine = Engine('main')

    # run the game
    gameRunner(active)
