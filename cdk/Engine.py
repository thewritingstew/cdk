# import statements
from Game import *

##
class Engine(object):

    # TODO Would I create the game objects here? Probably not.

    def __init__(self, eType):

        # set type of engine
        self.type = eType
        # TODO create game objects

        # call appropriate menu
        self.menuBuilder(eType)

    ##
    # TODO create some functions as needed...maybe menu creator
    ##
    def menuBuilder(self, m):

        if m == 'default':
            self.menuList = [
                "Quit", # TODO want to get rid of this one later...move to two menu lists
                "Carson's game",
                "Davis' game",
            ]
        elif m == 'main':
            self.menuList = [
                "Quit"
            ]

    ##
    # this is for doing things with the choice
    ##
    def useChoice(self, int):
        # handle the menu choice
        # menu choice 1
        if self.type == 'default':
            if int == 0:
                print "This should never print."
            elif int == 1:
                print "Playing Carson's game now."
            else:
                print "Playing Davis' game now."
