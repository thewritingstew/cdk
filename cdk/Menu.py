# this file holds the menus for the cdk game

class Menu(object):
    
    ## START TODO
    # This function will be used to establish the list of valid menu items.
    # It will write to an array, or maybe it would be better to use a 
    # dictionary, since I could put a key as the number and the value as 
    # the menu text.
    ## END TODO
    def __init__(self, e_gameList):
    
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
        # TODO replace this with an argument passed from the Engine.py class.
        self.menuOptions = e_gameList

        # decorative starting content for menu
        self.menuDecoration = 70*'=' # horizontal rule
        
    def showMenu(self, promptChar):
        # capture the prompt text for use in the menu
        prompt = promptChar
        
        # put menu decorations onto the page to break things up
        print self.menuDecoration

        # put intro text to screen 
        print self.welcomeText
        
        # put menu options to screen
        print
        for entry in self.menuOptions:
            print '\t' + entry + '\t' + self.menuOptions[entry]
        
        # put make selection prompt
        print
        print self.promptText
        
        # take in the choice
## TODO
# Check for a valid integer entry for the menu selection
# If things are valid, return the number chosen
# Else return the error value
        usrChoice = int(raw_input(prompt))

        
        return usrChoice
