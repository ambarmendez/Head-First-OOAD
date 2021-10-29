'''
    Simulation of a typical day for Rick now ... a customer comes in, tells him what they like,
    and he runs a search on his inventory.
'''
from inventory import Inventory
from guitar import Guitar, GuitarSpec, Builder, Type, Wood


def initialize_inventory(inventory):
    ''' set up Rick's guitar inventory '''
    inventory.add_guitar('A4565767', 2541.23, GuitarSpec(Builder.GIBSON, 'DE-5', Type.ACOUSTIC, Wood.MAHOGANY, Wood.INDIAN_ROSEWOOD))
    inventory.add_guitar('V95693', 1499.95, GuitarSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER))
    inventory.add_guitar('sr112233', 5687.53, GuitarSpec(Builder.MARTIN, 'mo-98', Type.ELECTRIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ALDER))
    inventory.add_guitar('V9512', 1549.95, GuitarSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER))


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    # Erin is looking for an Fender 'Strat' guitar, made of Alder
    what_erin_likes = GuitarSpec(Builder.FENDER, 'Stratocastor', Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
    matching_guitars = inventory.search(what_erin_likes)

    if matching_guitars:
        print('Erin, you might like these guitars: ')
        for guitar in matching_guitars:
            print(
                'We have a {} {} {} guitar:\n\t{} back and sides, \n\t{} top.\nYou can have it for only ${}!\n---'
                .format(
                    guitar.guitar_spec.builder,
                    guitar.guitar_spec.model,
                    guitar.guitar_spec.type,
                    guitar.guitar_spec.backwood,
                    guitar.guitar_spec.topwood,
                    guitar.price)
            )
    else:
        print('Sorry, Erin, we have nothing for you.')


if __name__ == '__main__':
    main()
