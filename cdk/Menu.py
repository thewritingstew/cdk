# this file holds the menus for the cdk game

class Menu(object):

    # START TODO
    # This function will be used to establish the list of valid menu items.
    # It will write to an array, or maybe it would be better to use a
    # dictionary, since I could put a key as the number and the value as
    # the menu text.
    # END TODO
    def __init__(self, e_gameList):

        # define the variables
        self.menuOptions = {}
        # TODO take the menu text and put it into another file.
        self.welcomeText = (
            "Welcome to Crags and Danger Kingdom!\n"
            "What would you like to do today?"
        )

        # text that appears after the menu options are printed.
        self.promptText = (
            "Please make your selection below:"
        )

        # menu options as a dictionary for easy handling on print.
        # TODO replace this with a for loop to iterate through the passed array
        self.list = range( len(e_gameList) )
        for i in self.list:
            self.menuOptions[self.list[i]] = e_gameList[i]

        # decorative starting content for menu
        self.menuDecoration = 70*'=' # horizontal rule

    def showMenu(self):

        # put menu decorations onto the page to break things up
        print self.menuDecoration

        # put intro text to screen
        print self.welcomeText

        # put menu options to screen
        print
        for entry in self.menuOptions:
            print '\t' + str(entry) + '\t' + self.menuOptions[entry]

    def checkValid(self, choice):

        # if choice is an int in range list,
        if choice in self.list:
            # then respond with that int
            return 1
        # else respond with that item isn't valid, please choose again
        else:
            return 0

    def badChoice(self):
        print "That choice is not an option."
        print "Please make another selection."
