# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []

    def take_item(self, item):
        self.items.append(item)
        self.current_room.remove_item(item)
        print(f'You pick up {item.name} and inspect it...\n')
        print(f'{item.description}\n')
    
    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.add_item(item)
        print(f'You dropped {item.name}\n')