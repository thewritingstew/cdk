# Design Doc for Crags and Danger Kingdom
Crags and Danger Kingdom is a text-based adventure game. The players wake up
in a room they don't recognize, and must navigate through the rest of the
rooms until they reach the Portal Room, which will take them back to their
native land. 

# Scenes
## Starting Room
This is the room where the player "wakes up" and realizes they don't know what
is going on. Nothing interesting happens here, except that the player is given
the choice of direction to go. 

## Supply Room
Supply rooms will have weapons, food, et. The items in these rooms can be
added to the player's inventory. 

## Danger Room
Danger rooms will have some kind of danger that must be escaped by physical
conflict. These rooms differ from puzzle rooms in that the challenges in the
danger room affect the player's health, not their energy level. 

## Puzzle Room
Puzzle rooms will have some kind of puzzle to losve before advancing. These
rooms will cost the player some energy.

## Recuperate Room
These rooms are empty rooms that allow users to rest, which adds to their
energy level, and to eat, which adds to their health level. 

## Portal Room
The portal room is the finish line. If the user makes it to the portal room,
they can safely return to their own land.

# Classes
Note: A plus sign, +, indicates a method. A dash, -, indicates an attribute.
## Class: Engine
## Class: Door
## Class: Player
## Class: Item
## Class: Scene
## Class: Map 
## Class: Game

