'''
It takes care of troops, armies, and all the units used in a game
'''
class Unit:
    ''' It supports all types of units by having type, id, name, and weapons as
    common properties share among all units. Any number of different attributes
    that varies among each game-specific requirement goes inside the general
    properties '''
    def __init__(self, id):
        self._id = id
        self.type = ''
        self.name = ''
        self.weapons = None
        self.properties = None

    @property
    def id(self):
        return self._id

    def add_weapon(self, weapon):
        ''' It waits until there is a need for a weapons list to instantiate a
        new list. That saves a little bit of memory, especially when there may
        be a thousands of units '''
        if self.weapons is None:
            self.weapons = []
        self.weapons.append(weapon)

    def set_property(self, property, value):
        ''' Just like weapons list, a dictionary is not created until it is nedeed '''
        if self.properties is None:
            self.properties = {}
        self.properties[property] = value

    def get_property(self, property):
        ''' Since properties might not be initialized, there is an extra check before
        looking up a property's value '''
        if self.properties is None:
            return None
        if property in self.properties:
            return self.properties[property]
        return None
