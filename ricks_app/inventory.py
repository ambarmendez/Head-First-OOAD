from instrument import Instrument, InstrumentSpec, Guitar
from instrument import GuitarSpec, MandolinSpec, Mandolin

class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, serial_number, price, spec):
        ''' It takes in all the properties required to create a new instrument
        instance, creates a Guitar or Mandolin object, and adds it to the Rick's
        inventory
        '''
        instrument = None
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serial_number, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serial_number, price, spec)
        self.instruments.append(instrument)

    def get(serial_number):
        for instrument in self.instruments:
            if instrument.serial_number == serial_number:
                return instrument
        else:
            return None

    def search(self, search_spec):
        ''' It takes in a client's ideal guitar, and returns a guitar from Rick's Inventory
        that matches up with the client's spec.
        '''
        matching_guitars = []
        for guitar in self.instruments:
            if guitar.spec == search_spec:
                matching_guitars.append(guitar)

        return matching_guitars

    def search_mandolins(self, specification):
        ''' There is two search methods one for guitars and other for mandolins because it
        doesn't make sense to have one method that return both mandolins and guitars since
        a spec will match only other specs of the same instrument type.
        '''
        matching_mandolins = []
        for mandolin in self.instruments:
            if specification == mandolin.spec:
                matching_mandolins.append(mandolin)

        return matching_mandolins
