from guitar import Guitar

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, type, backwood, topwood):
        ''' It takes in all the properties required to create a new Guitar instance, creates
        a Guitar object, and adds it to the Rick's inventory
        '''
        guitar = Guitar(serial_number, price, builder, model, type, backwood, topwood)
        self.guitars.append(guitar)

    def get_guitar(serial_number):
        for guitar in self.guitars:
            if guitar.serial_number == serial_number:
                return guitar
        else:
            return None

    def search(self, search_guitar):
        ''' It takes in a client's ideal guitar, and returns a guitar from Rick's Inventory
        that matches up with the client's spec.
        '''
        matching_guitars = []
        for guitar in self.guitars:
            if search_guitar.builder != guitar.builder:
                continue
            if not search_guitar.model and search_guitar.model.lower() != guitar.model.lower():
                continue
            if search_guitar.type != guitar.type:
                continue
            if search_guitar.backwood != guitar.backwood:
                continue
            if search_guitar.topwood != guitar.topwood:
                continue
            matching_guitars.append(guitar)

        return matching_guitars
