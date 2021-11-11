from .dogdoor import DogDoor

class BarkRecognizer:
    def __init__(self, dogdoor):
        '''
        It stores the dog door that this bark recognizer is attached to
        '''
        self.door = dogdoor

    def recognize(self, bark):
        '''
        Every time the hardware hears a bark, it will call this method with the
        sound of the bark instead
        '''
        print('\tBarkRecognizer: Heard a "{}"'.format(bark))
        self.door.open()
