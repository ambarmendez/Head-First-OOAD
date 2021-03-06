import threading


class DogDoor:
    '''
    Interface with Doug's custom door hardware, which means it will control
    the hardware in Todd and Gina's dog door
    '''
    def __init__(self):
        self.state = False
        self.allowed_barks = []

    def open(self):
        print('The dog door opens.')
        self.state = True

        t = threading.Timer(5, self.close)
        t.start()

    def close(self):
        print('The dog door closes.')
        self.state = False

    def is_open(self):
        '''
        It returns the state of the door, whether it's open or closed
        '''
        return self.state

    def add_allowed_bark(self, bark):
        self.allowed_barks.append(bark)
