from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
room['overlook'].add_item(Item('Key', """A key, begrimed and dull--except for 
a small glint at its bit."""))
room['treasure'].add_item(Item('Parchment', """A parchment with a list of tresure, presumabely
taken from this room. Under this, an
additional note:
'Next stop: an unnamed island to the west.'"""))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def move_direction(direction):
    dir_exists = False
    dir = None
    if direction == 'n':
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            dir_exists = True
            dir = 'north' 
    if direction == 's':
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            dir_exists = True
            dir = 'south'
    if direction == 'e':
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
            dir_exists = True
            dir = 'east'
    if direction == 'w':
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
            dir_exists = True
            dir = 'west'
    if dir_exists:
        print(f'You move {dir}\n')
    else:
        print('You cannot go that way.\n')

while True:
    # print room info
    print(f'*** {player.current_room.name} ***')
    print(f'{player.current_room.description}\n')
    
    # print room items
    if len(player.current_room.items) > 0:
        print('You see the following items:')

        # print out all the items that are in this room
        for item in player.current_room.items:
            print(f'* {item.name}')
        print('\n')

    # prompt the user for input
    cmd = input("Command: ")

    # quit the game
    if cmd == 'q':
        break

    # player is moving in a direction
    elif cmd == 'n' or cmd == 's' or cmd == 'e' or cmd == 'w':
        move_direction(cmd)

    # player did not enter a valid command
    else:
        print('Invalid command.\n')
