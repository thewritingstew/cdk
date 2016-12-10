"""
This module creates the context object, which is the foundational object for 
every context that displays things and takes input from the user. 
"""

class Context(object):
    
    def __init__(self, name="", init_display=""):
        """
        Initializes a Context object. 
        :param name: string 
        :return: None
        """
        self.context_name = name  # name of the context
        self.action_paths = {
            'quit':("Quit the game", False),
            'help':("Get help", ("Type 'hint' to get a list of available actions (if any), "
                "'q' to return to main menu, "
                "or 'quit' to exit the game entirely."
                ))
            }  # list of navigation contexts, help, quit
        self.hints_on = True  # boolean telling whether hints are allowed
        self._goto_context = self  # goto points to self for now
        self._initial_display = init_display  # set initial display

    def execute_choice(self):  # TODO: delete this? Not sure what it does.
        pass


    def update_action_paths(self, context_list):        
        for key in context_list:
            self.action_paths[key] = context_list[key]


    def get_hints(self):  # TODO: update to format dictionary for printing
        if self.hints_on:
            print(
                "\n",
                "%10s" % "COMMAND",  # column 1 header
                " " * 4,  # print four spaces
                "ACTION"  # column 2 header
            )
            for key in sorted(self.action_paths):  # iterate through action_paths dict
                print(
                      "%10s" % key,  # print the key, 10 characters wide
                      " " * 4,  # print four spaces
                      self.action_paths[key][0]  # print the dict value
                      )
            print("\nPlease type a command from the list above.")
        else:
            print("Sorry, no hints available from here. Try typing 'help'",
                " for help or 'q' to return to the main menu.")


    # TODO: Update this to print the Context object
    # def __repr__(self):
        # """
        # Create a basic functionality for printing nicely
        # :return: a string
        # """
        # return ""  


    # current_context.display()  # display current context's display
    def display(self, prior_context=""):
        # TODO: pretty up this print function
        print("~"*70)
        print("~"*70)
        if self._initial_display != "":  # displays initial display if not blank
            print(self._initial_display)
        else:
            self.get_hints()  # use get_hints for printing

        
        
    # current_context.get_input()  # process the user's input
    def get_input(self):
        # process the input for the current context
        usr_input = input("\nWhat would you like to do? ==> ")  # get input
        # print("User input is: {}".format(usr_input))  # DEBUG
        self._process_input(usr_input)  # process the input

        
    # current_context = current_context.next_context()  # get next context
    def next_context(self):
        """
        Return the next context to go to 
        :return: context
        """
        return(self._goto_context)
        

    def _process_input(self, usr_in):
        command = usr_in.split()[0]
        
        ### if dict keys are not integers, then this try isn't needed
        # try:  # change input from string to int if applicable
        #   # command = int(command)
        # except ValueError:
        #   # pass
        ###
        
        if command == 'q':  # alternate of 'quit'
            self._goto_context = self.action_paths['quit'][1]
        elif command == 'h' or command == 'help':  # alternate of 'help'
            print(self.action_paths['help'][1])  # TODO: iss #6 temp fix
            # self._goto_context = self.action_paths['help'][1]
        elif command in self.action_paths:
            self._goto_context = self.action_paths[command][1]
        else:
            self._goto_context = self
            
# end of file
