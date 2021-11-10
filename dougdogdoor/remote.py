from .dogdoor import DogDoor

class Remote:
    '''
    To allow a remote control to operate the dog door
    '''
    def __init__(self, dogdoor):
        '''
        Initialize the communication with the dog door object
        '''
        self.door = dogdoor

    def press_button(self):
        '''
        It controls the dog door
        '''
        print('Pressing the remote control button...')
        if self.door.is_open():
            self.door.close()
        else:
            self.door.open()
