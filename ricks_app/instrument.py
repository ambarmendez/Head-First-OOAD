from abc import ABC
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


class Style(Enum):
    A = 1
    F = 2

    def describe(self):
        return self.name, self.value

    def __str__(self):
        if self.value == 1:
            return 'A'
        if self.value == 2:
            return 'F'


class InstrumentSpec(ABC):
    ''' It is an abstract base class for GuitarSpec and MandolinSpec, it has all
        the common specifications for both
    '''
    def __init__(self, builder, model, type, backwood, topwood):
        ''' It receives a set of general and common specifications that clients
        are interested in finding in their ideal instrument: the woods used, or
        the type of guitar, or a particular builder or model.
        '''
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood

    def __eq__(self, obj):
        ''' It compare two InstrumentSpec instances. It returns True if two
        InstrumentSpec objects have the same builder, model, type, backwood
        and topwood.
        '''
        if not isinstance(obj, InstrumentSpec):
            return False
        if obj.builder != self.builder:
            return False
        if not obj.model and obj.model.lower() != self.model.lower():
            return False
        if obj.type != self.type:
            return False
        if obj.backwood != self.backwood:
            return False
        if obj.topwood != self.topwood:
            return False
        return True


class GuitarSpec(InstrumentSpec):
    '''
    Client's specifications for the ideal guitar
    '''
    def __init__(self, num_strings, builder, model, type, backwood, topwood):
        ''' It receives a set of general specifications that clients are
        interested in finding in their ideal guitar: the woods used, or
        the type of guitar, or a particular builder or model.
        '''
        super().__init__(builder, model, type, backwood, topwood)
        self.num_strings = num_strings

    def __eq__(self, obj):
        ''' It compare two GuitarSpec instances. It returns True if two
        GuitarSpec objects have the same specifications plus amount of strings.
        '''
        if not super().__eq__(obj):
            return False
        if not isinstance(obj, GuitarSpec):
            return False
        if obj.num_strings != self.num_strings:
            return False
        return True


class MandolinSpec(InstrumentSpec):
    ''' Client's specifications for the ideal guitar '''
    def __init__(self, builder, model, tyype, style, backwood, topwood):
        ''' It receives a set of general specifications that clients are
        interested in finding in their ideal mandolin plus style.
        '''
        super().__init__(builder, model, tyype, backwood, topwood)
        self.style = style

    def __eq__(self, obj):
        ''' It compare two MandolinSpec instances. It returns True if two
        MandolinSpec objects have the same general specifications plus style.
        '''
        if not super().__eq__(obj):
            return False
        if not isinstance(obj, MandolinSpec):
            return False
        if obj.style != self.style:
            return False
        return True


class Instrument(ABC):
    ''' It is a base class for Guitar and Mandolin, it has all the attributes
        and operations that are common to both. There is no such thing as an
        actual "instrument". Currently, instrument has no behaviour outside of
        its subclasses. '''
    def __init__(self, serial_number, price, instrument_spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = instrument_spec


class Guitar(Instrument):
    '''
    Each guitar in Rick's inventory is represented by an instance of this class
    '''
    def __init__(self, serial_number, price, guitar_spec):
        ''' Define all the characteristics of a guitar:
        - Properties that are unique to each particular guitar: the serial number and
        how much does it costs.
        - Some other general specifications.
        '''
        super().__init__(serial_number, price, guitar_spec)


class Mandolin(Instrument):
    ''' Each mandolin in Rick's inventory is represented by an instance of this class '''
    def __init__(self, serial_number, price, mandolin_spec):
        ''' Defining characteristics that makes a unique mandolin: the serial number,
        how much does it costs plus some other general specifications
        '''
        super().__init__(serial_number, price, mandolin_spec)        
