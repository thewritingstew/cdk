"""
This module creates the context object, which is the foundational object for 
every context that displays things and takes input from the user. 
"""

class Context(object):
    
    def __init__(
                self, name="", 
                init_display="", 
                hint_description="",
                quit=False,  # TODO: combine quit and help into one
                help=False  # TODO: call the combined support_type
                ):
        """
        Initializes a Context object. 
        :param name: string 
        :return: None
        """
        self.name = name  # name of the context
        self.hint_description = hint_description  # description for hint menu
        self.context_path = (self.hint_description, self)
        self.action_paths = {}  # dict in str:(str, context) format
        self.hints_on = True  # boolean telling whether hints are allowed
        self._goto_context = self  # goto points to self for now
        self._initial_display = init_display  # set initial display
        self.caller_context = self  # context that called this context
        self.help_type = help  # determine if this is help type context
        self.quit_type = quit  # determine if this is quit type context

    def execute_choice(self):  # TODO: delete this? Not sure what it does.
        pass


    def update_action_paths(self, context_list):
        """
        Updates the action paths for a context.
        :parameter context_list: a tuple of tuples where, for each inner tuple, 
            [0] is the string that is the command to go to the context, and 
            [1] is a context.
        """
        for item in context_list:
            self.action_paths[item[0]] = item[1].context_path


    def get_hints(self):  # TODO: update to format dictionary for printing
        if self.hints_on:
            print(
                "\n%10s" % "COMMAND",  # column 1 header
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
        if self.name != '::help' and self.name != '::quit':
            try:
                self._goto_context.caller_context = self
            except AttributeError:
                pass
        return(self._goto_context)
        

    def _process_input(self, usr_in):
        command = usr_in.split()[0]
        quit_commands = ('::q', '::quit', 'q', 'quit')  # alternates of quit
        help_commands = ('::h', '::help', 'h', 'help')  # alternates of help

        if command in quit_commands:
            self._goto_context = self.action_paths['::quit'][1]
        elif command in help_commands:
            self._goto_context = self.action_paths['::help'][1]
        elif command == '::r':
            self._goto_context = self.caller_context  # send back to caller
        elif command == '::hint::':
            self.get_hints()
        elif command in self.action_paths:
            self._goto_context = self.action_paths[command][1]
        else:
            self._goto_context = self
            
# end of file
