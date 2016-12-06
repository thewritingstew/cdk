"""
This module creates the context object, which is the foundational object for 
every context that displays things and takes input from the user. 
"""

class Context(object):
    
    def __init__(self, name=""):
        self.context_name = name
        self.support_paths = []  # support contexts 'help' and 'quit'
        self.action_paths = []  # navigation contexts        
        self.hints_on = True  # boolean telling whether hints are allowed


    def execute_choice(self):
        pass


    def update_action_paths(self, context_list):
        
        for item in context_list:
            if self.action_paths.count(item.context_name) > 0:
                # the item is in the list, so alert user
                print("'{}' is already a member of the list.".\
                      format(item.context_name))
            else:
                self.action_paths.append(item.context_name)

    def get_hints(self):
        if self.hints_on:
            for i, j in enumerate(self.action_paths):  # unpack tuple to i, j
                print(
                      "\t",  # print a tab to move things over
                      "%4d" % i,  # print the index in four characters
                      " " * 4,  # print four spaces
                      j  # print the list item
                      )  
        else:
            print("Sorry, no hints available from here. Try typing '::help'")


# end of file
