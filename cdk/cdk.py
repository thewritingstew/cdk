"""
Starts the CDK game engine. It is from here that things are processed.
"""
# import statements
from context import Context
import rooms as rm

def create_default_actions():
    game_items, help_items = rm.build_contexts()
    
    default_menu_items = [(str(game_items.index(item)), item)
        for item 
        in game_items
        ]
    default_menu_items.extend([(item.name, item) 
        for item 
        in help_items
        ])
        
    print(default_menu_items)

    return default_menu_items


def main():
    """
    runs the game
    """
    main_menu = Context()  # create the main menu context
    current_context = main_menu  # set main_menu as current context
    
    # print("Before: ", main_menu.action_paths)  # DEBUG

    action_list = create_default_actions()  # create default set of games
    main_menu.update_action_paths(action_list)  # add games to menu
    
##    print(main_menu.support_paths)
    # print("After: ", main_menu.action_paths)  # DEBUG
    
    while True:
        # TODO: if current_context.skip_to == empty, then do what we have already 
        # defined below. Otherwise, set current_context to something else and 
        # return to top of while loop. This will be accomplished with the if-
        # else, but we could also use a 'continue' to jump back to the top of 
        # the loop and try it again. 
        current_context.display()  # display current context's display
        current_context.get_input()  # process the user's input
        current_context = current_context.next_context()  # get next context
        if not current_context:
            break


if __name__ == "__main__":
    main()  # sets up and plays the game (maybe break out someday)
    exit(0)
