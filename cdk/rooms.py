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
    c1 = Context(
        name="Start", 
        init_display=(
            "You wake up. You are lying on your back. "
            "You start to roll over, but your elbow hits "
            "something hard. Whatever it is grates against the floor. "
            "You move your body, which is tired and slow, away from the "
            "object on the ground and sit up. The object is a shield. It "
            "must be your shield, since it is attached to your arm. "
            "You try to look around the room, but discover that it is dark. "
            "The area immediately around you isn't very clean, and you expect "
            "that you'll find the rest of the room in equally poor condition. "
            "You look around, and discover that there are doors to the east, "
            "the west, and the north.\n\n"
            "Which direction would you like to go (type 'north', 'west', "
            "or 'east' to move"
            ),
        # alt_display=(
            # "You're back in the room you started in. There are "
            # "doors to the north, the east, and the west."
            # ),
        hint_description="Start of Carson's game",
        )
    c2 = Context(
        name='weapons',
        init_display=(
            "The door creaks as you enter the room. Across the room there "
            "is a table with several items on it, illuminated by a light "
            "coming from somewhere. Looking around the rest of the room you "
            "find the source of the light. There are several holes in the "
            "ceiling, and they are letting in light. You can't make out the "
            "source of the light. It's bluish tint means it must not be "
            "sunlight.\n\nYou walk over to the table and discover three "
            "swords. A note on the table reads: "
            "\n\n\tYou're         land under,"
            "\n\n\tbut how         wonder,"
            "\n\n\tgo back to the      "
            "\n\n\t  sword you must take,"
            "\n\n\tq       s  s    your way."
            "\n\nWhich sword will you take? Your choices are 'wood', "
            "'titanium', and 'diamond'."
            ),
        hint_description="weapons room",
        )
    
    c2_w = Context(
        name='wood',
        init_display=(
            "The wood sword is heavy in your hand, but it seems to match "
            "the environment your are in. Feeling a bit more prepared with "
            "a sword to go with your shield, you decide you'd better start "
            "whatever it is you are doing. You turn back toward the room "
            "and notice there is only one door, to the west."
            ),
        hint_description="weapons room",
        )

    c2_d = Context(
        name='diamond',
        init_display=(
            "The diamond sword is heavy in your hand, but the jeweled handle "
            "matches your jeweled shield. Feeling a bit more prepared with "
            "a sword to go with your shield, you decide you'd better start "
            "whatever it is you are doing. You turn back toward the room "
            "and notice there is only one door, to the west."
            ),
        hint_description="weapons room",
        )

    c2_t = Context(
        name='titanium',
        init_display=(
            "The titanium sword is heavy in your hand, but its weight and "
            "solidness put you at ease. Feeling a bit more prepared with "
            "a sword to go with your shield, you decide you'd better start "
            "whatever it is you are doing. You turn back toward the room "
            "and notice there is only one door, to the west."
            ),
        hint_description="weapons room",
        )

    c1_e = Context(
        name='start',
        init_display=(
            "You return to the room you started in. It is still dark, but "
            "you can tell you are still alone. Two closed doors still stand "
            "to the north and to the west."
            ),
        hint_description="start room",
        )

    c3 = Context(name='dragon')  # wood doesn't work, no sword and you die
    c4 = Context(name='potions')  # two potions, one kills
    c5 = Context(name='friend')  # kill the image of a friend?
    c6 = Context(name='rest')  # take a break to gather strength
    c7 = Context(name='monkeys')  # choose fight or run. w and d swords work
    c8 = Context(name='portal')  # portal back to home world...no troubles for rest of life
    
    # TODO: update action paths
    g1.update_action_paths([("start", c1)])
    c1.update_action_paths([("east", c2), ("north", c3), ("west", c4)])
    c2.update_action_paths([("west", c1), ('wood', c2_w), 
        ('diamond', c2_d), ('titanium', c2_t) ])
    c2_d.update_action_paths([('west', c1_e)])
    c2_w.update_action_paths([('west', c1_e)])
    c2_t.update_action_paths([('west', c1_e)])

    context_list.extend([  # add to list needing help and quit
        c1, c1_e, 
        c2, c2_w, c2_d, c2_t, 
        c3, 
        c4,
        c5,
        c6,
        c7,
        c8
        ])
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

