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
            

class Guitar:
    ''' Each guitar in Rick's inventory is represented by an instance of this class '''
    def __init__(self, serial_number, price, builder, model, type, backwood, topwood):
        ''' Defining characteristics of a guitar: the serial number, how much does it
        costs, the builder and the model, what type it is (acoustic or electric), and
        what woods are used in the guitar.
        '''
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood
