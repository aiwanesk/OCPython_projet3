class Macgyver:
    """The hero, MacGyver, with the coordinates of his position, his name and
    if he had loot objects"""

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.loot = [False, False, False]  # liste de loot
