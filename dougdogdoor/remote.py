from .dogdoor import DogDoor

import threading


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
        It controls the dog door, which toggles between opening and closing the
        door
        '''
        print('Pressing the remote control button...')
        if self.door.is_open():
            self.door.close()
        else:
            self.door.open()
