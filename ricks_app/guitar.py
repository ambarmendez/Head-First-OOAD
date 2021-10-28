class Guitar:
    ''' Each guitar in Rick's inventory is represented by an instance of this class '''
    def __init__(self, serial_number, price, builder, model, type, backwood, topwood):
        ''' Defining characteristics of a guitar: the serial number, how much does it
        costs, the builder and the model, what type it is (acoustic or electric), and
        what woods are used in the guitar.
        '''
        self.serial_number = serial_number
        self.price = price
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood
