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

def move(direction):
    directions = ['north', 'south', 'east', 'west']

    # gets the print-friendly direction based on
    # the user's input
    print_dir = [d for d in directions if d[0] == direction][0]

    # find the next room based on the direction attr
    dir_attr = f'{direction}_to'
    next_room = getattr(player.current_room, dir_attr)

    # you can go in this direction
    if next_room is not None:
        player.current_room = next_room
        print(f'You move {print_dir}\n')

    # you cannot go in this direction
    else:
        print('You cannot go that way.\n')

# gets an item in the room by its string name
def get_item_in_room_by_name(name):
    for item in player.current_room.items:
        if item.name == name:
            return item
    return None

# gets an item in the user's inventory by its string name
def get_item_in_inventory_by_name(name):
    for item in player.items:
        if item.name == name:
            return item
    return None

def open_inventory():
    if len(player.items) == 0:
        print('Inventory is empty\n')
    else:
        print('Inventory:\n')
        for item in player.items:
            print(f'* {item.name}')
            print(f'{item.description}\n')

def help():
    print("""
    Available commands:
    * n - move north
    * s - move south
    * e - move east
    * w - move west
    * take [item] - take an item
    * drop [item] - drop an item
    * i - open inventory
    * q - quit the game
    """)

def announce_room():
    print(f'*** {player.current_room.name} ***')
    print(f'{player.current_room.description}\n')

exit = False
is_start = True # true when the user has 

while not exit:
    # print room info
    if is_start:
        announce_room()
    
    # print room items
    if len(player.current_room.items) > 0:
        print('You see the following items:')

        # print out all the items that are in this room
        for item in player.current_room.items:
            print(f'* {item.name}')
        print('\n')

    # prompt the user for input
    cmd = input("What is your next step? ")
    is_start = False
    cmdWithArgs = cmd.split(' ')

    # display help
    if cmd == 'help':
        help()

    # quit the game
    elif cmd in ['q', 'quit', 'exit']:
        exit = True

    # player is moving in a direction
    elif cmd in ['n', 's', 'e', 'w']:
        move(cmd)
        announce_room()

    # player is viewing inventory
    elif cmd in ['i', 'inventory']:
        open_inventory()

    elif len(cmdWithArgs) > 1:
        # player has a command with more than one word
        if cmdWithArgs[0] == 'take':
            # user is picking up an item
            item = get_item_in_room_by_name(cmdWithArgs[1])
            player.take_item(item)
        if cmdWithArgs[0] == 'drop':
            # user is dropping an item
            item = get_item_in_inventory_by_name(cmdWithArgs[1])
            player.drop_item(item)

    # player did not enter a valid command
    else:
        print('Invalid command.\n')
