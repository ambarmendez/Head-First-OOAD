from enum import Enum


class Type(Enum):
    ACOUSTIC = 1
    ELECTRIC = 2

    def __str__(self):
        if self.value == 1:
            return 'acoustic'
        if self.value == 2:
            return 'electric'


class Builder(Enum):
    FENDER = 1
    MARTIN = 2
    GIBSON = 3

    def __str__(self):
        if self.value == 1:
            return 'Fender'
        if self.value == 2:
            return 'Martin'
        if self.value == 3:
            return 'Gibson'


class Wood(Enum):
    INDIAN_ROSEWOOD = 1
    BRAZILIAN_ROSEWOOD = 2
    MAHOGANY = 3
    ALDER = 4
    SITKA = 5

    def __str__(self):
        if self.value == 1:
            return 'Indian Rosewood'
        if self.value == 2:
            return 'Brazilian Rosewood'
        if self.value == 3:
            return 'Magohany'
        if self.value == 4:
            return 'Alder'
        if self.value == 5:
            return 'Sitka'


class GuitarSpec:
    '''
    Client's specifications for the ideal guitar
    '''
    def __init__(self, builder, model, type, backwood, topwood):
        ''' It receives a set of general specifications that clients are
        interested in finding in their ideal guitar: the woods used, or
        the type of guitar, or a particular builder or model.
        '''
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood


class Guitar:
    '''
    Each guitar in Rick's inventory is represented by an instance of this class
    '''
    def __init__(self, serial_number, price, guitar_spec):
        ''' Define all the characteristics of a guitar:
        - Properties that are unique to each particular guitar: the serial number and
        how much does it costs.
        - Some other general specifications.
        '''
        self.serial_number = serial_number
        self.price = price
        self.guitar_spec = guitar_spec
