'''
    Simulation of a typical day for Rick now ... a customer comes in, tells him what they like,
    and he runs a search on his inventory.
'''
from inventory import Inventory
from instrument import GuitarSpec, Builder, Type, Wood


def initialize_inventory(inventory):
    ''' set up Rick's guitar inventory '''
    inventory.add_instrument('A4565767', 2541.23, GuitarSpec(4, Builder.GIBSON, 'DE-5', Type.ACOUSTIC, Wood.MAHOGANY, Wood.INDIAN_ROSEWOOD))
    inventory.add_instrument('V95693', 1499.95, GuitarSpec(6, Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER))
    inventory.add_instrument('sr112233', 5687.53, GuitarSpec(12, Builder.MARTIN, 'mo-98', Type.ELECTRIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ALDER))
    inventory.add_instrument('V9512', 1549.95, GuitarSpec(4, Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER))


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    # Erin is looking for an Fender 'Strat' guitar, made of Alder
    what_erin_likes = GuitarSpec(6, Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    matching_guitars = inventory.search(what_erin_likes)

    if matching_guitars:
        print('Erin, you might like these guitars: ')
        for guitar in matching_guitars:
            print(
                'We have a {} {} {}-strings {} guitar:\n\t{} back and sides, \n\t{} top.\nYou can have it for only ${}!\n---'
                .format(
                    guitar.spec.builder,
                    guitar.spec.model,
                    guitar.spec.num_strings,
                    guitar.spec.type,
                    guitar.spec.backwood,
                    guitar.spec.topwood,
                    guitar.price)
            )
    else:
        print('Sorry, Erin, we have nothing for you.')


if __name__ == '__main__':
    main()
