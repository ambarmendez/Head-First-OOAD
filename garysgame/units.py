'''
It takes care of troops, armies, and all the units used in a game
'''
class Unit:
    ''' It support all types of units, with any number of different types of
    properties and attributes '''
    def __init__(self):
        self.type = ''
        self.properties = {}
