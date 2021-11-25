'''
    Simulation of a typical day for Rick now ... a customer comes in, tells him what they like,
    and he runs a search on his inventory.
'''
from inventory import Inventory
from instrument import InstrumentSpec, InstrumentType, Builder, Type, Style, Wood


def initialize_inventory(inventory):
    ''' set up Rick's inventory '''
    inventory.add_instrument('11277', 3995.95, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.COLLINGS, 'model':'CJ', 'type':Type.ACOUSTIC, 'backwood':Wood.SITKA, 'topwood':Wood.INDIAN_ROSEWOOD}))
    inventory.add_instrument('122784', 5495.95, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.MARTIN, 'model':'D-18', 'type':Type.ACOUSTIC, 'backwood':Wood.ADIRONDACK, 'topwood':Wood.MAHOGANY}))
    inventory.add_instrument('V95693', 1499.53, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.FENDER, 'model':'stratocastor', 'type':Type.ELECTRIC, 'backwood':Wood.ALDER, 'topwood':Wood.ALDER}))
    inventory.add_instrument('V9512', 1549.95, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.FENDER, 'model':'stratocastor', 'type':Type.ELECTRIC, 'backwood':Wood.ALDER, 'topwood':Wood.ALDER}))
    inventory.add_instrument('82765501', 1890.95, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.GIBSON, 'model':"SG'61", 'type':Type.ELECTRIC, 'backwood':Wood.MAHOGANY, 'topwood':Wood.MAHOGANY}))
    inventory.add_instrument('70108276', 2295.95, InstrumentSpec({'instrument_type':InstrumentType.GUITAR, 'num_strings':6, 'builder':Builder.GIBSON, 'model':'Les Paul', 'type':Type.ELECTRIC, 'backwood':Wood.MAPLE, 'topwood':Wood.MAPLE}))
    inventory.add_instrument('9019920', 5495.99, InstrumentSpec({'instrument_type':InstrumentType.MANDOLIN, 'builder':Builder.GIBSON, 'model':'F5-G', 'type':Type.ACOUSTIC, 'style':Style.F, 'backwood':Wood.MAPLE,'topwood': Wood.MAPLE}))
    inventory.add_instrument('8900231', 2945.95, InstrumentSpec({'instrument_type':InstrumentType.BANJO, 'num_strings':5, 'builder':Builder.GIBSON, 'model':'RB-3', 'type':Type.ACOUSTIC, 'backwood':Wood.MAPLE}))


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    client_spec = InstrumentSpec({'builder':Builder.GIBSON, 'backwood':Wood.MAPLE})
    matching_instruments = inventory.search(client_spec)

    if matching_instruments:
        print('You might like these instruments: ')
        for instrument in matching_instruments:
            spec = instrument.spec
            print('We have a {} with the following properties:'.format(spec.properties['instrument_type']))
            for property in spec.properties:
                if property == 'instrument_type':
                    continue
                else:
                    print('\t{}: {}'.format(property, spec.properties[property]))
            print('  You can have this {} for ${}\n---'.format(spec.properties['instrument_type'], instrument.price))
    else:
        print('Sorry, we have nothing for you.')


if __name__ == '__main__':
    main()
