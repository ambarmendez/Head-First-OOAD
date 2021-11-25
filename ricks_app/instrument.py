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
    COLLINGS = 4
    def __str__(self):
        if self.value == 1:
            return 'Fender'
        if self.value == 2:
            return 'Martin'
        if self.value == 3:
            return 'Gibson'
        if self.value == 4:
            return 'Collings'


class Wood(Enum):
    INDIAN_ROSEWOOD = 1
    BRAZILIAN_ROSEWOOD = 2
    MAHOGANY = 3
    ALDER = 4
    SITKA = 5
    MAPLE = 6
    ADIRONDACK = 7

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
        if self.value == 6:
            return 'Maple'
        if self.value == 7:
            return 'Adirondack'


class Style(Enum):
    A = 1
    F = 2

    def __str__(self):
        if self.value == 1:
            return 'A'
        if self.value == 2:
            return 'F'


class InstrumentType(Enum):
    ''' So far, these are the types of instruments that Rick sells '''
    GUITAR = 1
    BANJO = 2
    DOBRO = 3
    FIDDLE = 4
    BASS = 5
    MANDOLIN = 6

    def __str__(self):
        ''' String version of what it is '''
        if self.value == 1:
            return 'Guitar'
        if self.value == 2:
            return 'Banjo'
        if self.value == 3:
            return 'Dobro'
        if self.value == 4:
            return 'Fiddle'
        if self.value == 5:
            return 'Bass'
        if self.value == 6:
            return 'Mandolin'
        return 'Unspecified'


class InstrumentSpec:
    ''' It is a class for string instruments, it has all the general specifications
        for the instruments
    '''
    def __init__(self, properties):
        ''' It receives a set of general and common specifications that clients
        are interested in finding in their ideal instrument.
        '''
        if properties:
            self.properties = dict(properties)
        else:
            self.properties = {}

    def __eq__(self, obj):
        ''' It compare two InstrumentSpec instances. It returns True if two
        InstrumentSpec objects have the same properties.
        '''
        if not isinstance(obj, InstrumentSpec):
            return False
        for property, value in obj.properties.items():
            if property not in self.properties or self.properties[property] != value:
                return False
        return True

    def get_property(self, property):
        ''' It returns a property value, None when is not there '''
        if property in self.properties:
            return self.properties[property]
        return None


# class GuitarSpec(InstrumentSpec):
#     '''
#     Client's specifications for the ideal guitar
#     '''
#     def __init__(self, num_strings, builder, model, type, backwood, topwood):
#         ''' It receives a set of general specifications that clients are
#         interested in finding in their ideal guitar: the woods used, or
#         the type of guitar, or a particular builder or model.
#         '''
#         super().__init__(builder, model, type, backwood, topwood)
#         self.num_strings = num_strings
#
#     def __eq__(self, obj):
#         ''' It compare two GuitarSpec instances. It returns True if two
#         GuitarSpec objects have the same specifications plus amount of strings.
#         '''
#         if not super().__eq__(obj):
#             return False
#         if not isinstance(obj, GuitarSpec):
#             return False
#         if obj.num_strings != self.num_strings:
#             return False
#         return True
#
#
# class MandolinSpec(InstrumentSpec):
#     ''' Client's specifications for the ideal guitar '''
#     def __init__(self, builder, model, tyype, style, backwood, topwood):
#         ''' It receives a set of general specifications that clients are
#         interested in finding in their ideal mandolin plus style.
#         '''
#         super().__init__(builder, model, tyype, backwood, topwood)
#         self.style = style
#
#     def __eq__(self, obj):
#         ''' It compare two MandolinSpec instances. It returns True if two
#         MandolinSpec objects have the same general specifications plus style.
#         '''
#         if not super().__eq__(obj):
#             return False
#         if not isinstance(obj, MandolinSpec):
#             return False
#         if obj.style != self.style:
#             return False
#         return True


class Instrument:
    ''' It is a class any string instrument, it has all the attributes
        and operations that are common to both. The behaviuor of each
        instrument doesn't vary. '''
    def __init__(self, serial_number, price, instrument_spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = instrument_spec
