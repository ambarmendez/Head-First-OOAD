from instrument import Instrument, InstrumentSpec


class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, serial_number, price, spec):
        ''' It takes in all the properties required to create a new instrument
        instance, creates a Guitar or Mandolin object, and adds it to the Rick's
        inventory
        '''
        instrument = Instrument(serial_number, price, spec)
        self.instruments.append(instrument)

    def get(serial_number):
        for instrument in self.instruments:
            if instrument.serial_number == serial_number:
                return instrument
        else:
            return None

    def search(self, search_spec):
        ''' It takes in a client's ideal guitar or mandolin, and returns a list
        of guitars or mandolins from Rick's Inventory that matches up with the
        client's spec.
        '''
        matching_instruments = []
        for instrument in self.instruments:
            if instrument.spec == search_spec:
                matching_instruments.append(instrument)

        return matching_instruments
