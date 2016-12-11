# import statements
from context import Context

context_list = []

def build_contexts():
    # for items in a file, import the default games and create contexts
    # for now these items will be hard-coded
    help = build_help()
    quit = build_quit()

    game_one = build_game_one()
    game_two = build_game_two()

    context_list.extend((game_one,game_two))  # add contexts to list
    
    # TODO: add more content to the default games, such as additional contexts
    # and the like. May want to pull the additional contexts out of a file,
    # rather than doing them all hard-coded. But hard-coded may be the easiest
    # answer right now just so I can finish this thing up and move on with
    # other programming tasks. 
    
    for context in context_list:
        h = (help.name, help)
        q = (quit.name, quit)
        help_and_quit = (h, q)
        context.update_action_paths(help_and_quit)
    
    default_menu_items = ((game_one, game_two), (help, quit))
    return default_menu_items

    
def build_game_one():
    g1 = Context(name="Carson's game",
        init_display="Welcome to Carson's game. Enter 'start' to proceed...",
        hint_description="Play Carson's game"
        )

    # TODO: create contexts
    
    # TODO: update action paths

    return g1


def build_game_two():
    g2 = Context(name="Davis's game",
        init_display="Welcome to Davis's game. Enter 'start' to proceed...",
        hint_description="Play Davis's game"
        )
        
    # TODO: create contexts
    
    # TODO: update action paths

    return g2

    
def build_help():
    h = Context(name='::help', 
                   init_display=("Type '::hint::' to get a list of available "
                                 "actions (if any), 'q' to return to main "
                                 "menu, or 'quit' to exit the game "
                                 "entirely. Type '::r' to return to the game."),
                   hint_description="Type 'h' to get help"
               )

    return h


def build_quit():
    q = Context(name='::quit',
                   init_display=("Are you sure you want to quit the game? "
                                 "Type 'y' to quit, '::r' to return to "
                                 "the game you are currently playing."),
                   hint_description="Type 'q' to quit the game"
               )
    q.action_paths["y"] = ("y", False)

    return q

