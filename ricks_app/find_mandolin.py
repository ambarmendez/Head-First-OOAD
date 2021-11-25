'''
    Simulation of a typical day for Rick now ... a customer comes in, tells him what they like,
    and he runs a search on his inventory.
'''
from inventory import Inventory
from instrument import Mandolin, MandolinSpec, Builder, Type, Style, Wood


def initialize_inventory(inventory):
    ''' set up Rick's guitar inventory '''
    inventory.add_instrument('serial_number', 0.23, MandolinSpec(Builder.GIBSON, 'model', Type.ACOUSTIC, Style.A, Wood.MAHOGANY, Wood.INDIAN_ROSEWOOD))
    inventory.add_instrument('V95693', 1499.95, MandolinSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER))
    inventory.add_instrument('sr', 0.53, MandolinSpec(Builder.MARTIN, 'm', Type.ELECTRIC, Style.A, Wood.BRAZILIAN_ROSEWOOD, Wood.ALDER))
    inventory.add_instrument('V95349', 1549.95, MandolinSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER))


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    specifications = MandolinSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER)
    matching_mandolins = inventory.search(specifications)

    if matching_mandolins:
        print('You might like these guitars: ')
        for mandolin in matching_mandolins:
            print(
                'We have a {} {} {}-style {} mandolin:\n\t{} back and sides, \n\t{} top.\nYou can have it for only ${}!\n---'
                .format(
                    mandolin.spec.builder,
                    mandolin.spec.model,
                    mandolin.spec.style,
                    mandolin.spec.type,
                    mandolin.spec.backwood,
                    mandolin.spec.topwood,
                    mandolin.price)
            )
    else:
        print('Sorry, we have nothing for you.')


if __name__ == '__main__':
    main()
