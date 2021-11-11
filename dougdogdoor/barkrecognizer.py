from .dogdoor import DogDoor

class BarkRecognizer:
    def __init__(self, dogdoor):
        '''
        It stores the dog door that this bark recognizer is attached to
        '''
        self.door = dogdoor

    def recognize(self, bark):
        '''
        Every time the hardware hears a bark, it will call this method with a
        Bark instance
        '''
        print('\tBarkRecognizer: Heard a "{}"'.format(bark.sound))
        for allowed_bark in self.door.allowed_barks:
            if allowed_bark == bark:
                self.door.open()
                return

        print('This dog is not allowed.')
