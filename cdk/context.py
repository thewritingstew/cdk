"""
This module creates the context object, which is the foundational object for 
every context that displays things and takes input from the user. 
"""

class Context(object):
    
    def __init__(self, name=""):
        """
        Initializes a Context object. 
        :param name: string 
        :return: None
        """
        self.context_name = name  # name of the context
        self.action_paths = {
            'quit':False,
            'help':False
            }  # list of navigation contexts, help, quit
        self.hints_on = True  # boolean telling whether hints are allowed
        self._goto_context = self


    def execute_choice(self):
        pass


    def update_action_paths(self, context_list):        
        for key in context_list:
            self.action_paths[key] = context_list[key]


    def get_hints(self):
        if self.hints_on:
            for i, j in enumerate(self.action_paths):  # unpack tuple to i, j
                print(
                      "\t",  # print a tab to move things over
                      "%4d" % i,  # print the index, four characters wide
                      " " * 4,  # print four spaces
                      j  # print the list item
                      )
            print("Please select an item from the list above.")
        else:
            print("Sorry, no hints available from here. Try typing '::help'")


    # current_context.display()  # display current context's display
    def display(self):
        # TODO: pretty up this print function
        print(self.action_paths)

        
        
    # current_context.get_input()  # process the user's input
    def get_input(self):
        # process the input for the current context
        usr_input = input("What would you like to do? ==> ")  # get input
        print("User input is: {}".format(usr_input))
        self._process_input(usr_input)  # process the input

        
    # current_context = current_context.next_context()  # get next context
    def next_context(self):
        # TODO: figure out what the next context is, and return it
        return(self._goto_context)
        

    def _process_input(self, usr_in):
        command = usr_in.split()[0]
        
        if command == 'quit' or command == 'q':  # could use if 'qu' in command
            self._goto_context = self.action_paths['quit']
        elif command in self.action_paths:
            self._goto_context = self.action_paths[command]
        else:
            self._goto_context = self
            
# end of file
