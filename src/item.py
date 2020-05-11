
class Item:
    def __init__(self, name, description):
        # check to see if the name has spaces in it
        if " " in name:
            raise ValueError('Item names must not have spaces')
        self.name = name
        self.description = description