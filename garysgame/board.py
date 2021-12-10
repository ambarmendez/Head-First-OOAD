'''
It handles the board itself, tiles, terrain, and other classes related to
creating the actual board used in each game
'''
class Tile:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.pop()


class Board:
    ''' Interface base that game designers can then use and extend to build their
    own games. The board's height and width are supplied by the game designers for
    their game. Additionally, the board can return the tile at a given position,
    add units to a tile, and return all the units at a given X-Y position'''

    def __init__(self, width, height):
        ''' It takes width and height, and creates a new board with that height
        and width. It also sets up the board '''
        self.width = width
        self.height = height
        self.tiles = []

        self._initializes()

    def _initializes(self):
        ''' It fills the board with square tiles, one at each X-Y position.
        BONUS DESIGN PRINCIPLE. Pull out setup code into its own method, so it
        doesn't make the rest of the code so confusing to read '''
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(Tile())
            self.tiles.append(row)

    def get_tile(self, x, y):
        ''' It returns the tile at a given position, given that tile's X and
        Y-position '''
        return self.tiles[x-1][y-1]

    def add_unit(self, unit, x, y):
        ''' It adds a unit to a tile based on that tile's X- and Y-position '''
        tile = self.get_tile(x, y)
        tile.add_unit(unit)

    def remove_unit(self, unit, x, y):
        ''' It removes a unit to a tile based on that tile's X- and Y-position '''
        tile = self.get_tile(x, y)
        tile.remove_unit(unit)

    def remove_units(self, x, y):
        ''' It removes all units to a tile based on that tile's X- and Y-position '''
        tile = self.get_tile(x, y)
        tile.remove_units()

    def get_units(self, x, y):
        ''' It returns all the units on a tile, given the X- and Y-position of
        the tile '''
        return self.get_tile(x, y).get_units()
