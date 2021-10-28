'''
    Simulation of a typical day for Rick now ... a customer comes in, tells him what they like,
    and he runs a search on his inventory.
'''
from inventory import Inventory
from guitar import Guitar


def initialize_inventory(inventory):
    ''' set up Rick's guitar inventory '''
    inventory.add_guitar('A4565767', 2541.23, 'Gibson', 'DE-5', 'acoustic', 'Mahogany', 'Indian Rosehood')
    inventory.add_guitar('V95693', 1499.95, 'Fender', 'Stratocastor', 'electric', 'Alder', 'Alder')
    inventory.add_guitar('sr112233', 5687.53, 'Martin', 'mo-98', 'electric', 'Brazilian_rosewood', 'Alder')
    inventory.add_guitar('V9512', 1549.95, 'Fender', 'Stratocastor', 'electric', 'Alder', 'Alder')


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    # Erin is looking for an Fender 'Strat' guitar, made of Alder
    what_erin_likes = Guitar('', 0, 'fender', 'Stratocastor', 'electric', 'Alder', 'Alder')
    guitar = inventory.search(what_erin_likes)

    if guitar:
        print('Erin, you might like this ', end='')
        print(
            '{} {} {} guitar:\n{} back and sides, \n{} top.\nYou can have it for only ${}!'
            .format(guitar.builder, guitar.model, guitar.type, guitar.backwood, guitar.topwood, guitar.price)
        )
    else:
        print('Sorry, Erin, we have nothing for you.')


if __name__ == '__main__':
    main()
