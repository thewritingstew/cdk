"""
Starts the CDK game engine. It is from here that things are processed.
"""
# import statements
from context import Context

def create_default_actions():
    # for items in a file, import the default games and create contexts
    # for now these items will be hard-coded
    game_one = Context(name="Carson's game")
    game_two = Context(name="Davis's game")

    # TODO: add more content to the default games, such as additional contexts
    # and the like. May want to pull the additional contexts out of a file,
    # rather than doing them all hard-coded. But hard-coded may be the easiest
    # answer right now just so I can finish this thing up and move on with
    # other programming tasks. 
    
    default_menu_items = {
        0:game_one,
        1:game_two
        }
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
        current_context.display()  # display current context's display
        current_context.get_input()  # process the user's input
        current_context = current_context.next_context()  # get next context
        if not current_context:
            break


if __name__ == "__main__":
    main()
    exit(0)
