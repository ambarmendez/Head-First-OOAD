class Bark:
    '''
    It manage everything related to the owner's dog's bark
    '''
    def __init__(self, sound):
        '''
        It store the sound of a dog's bark
        '''
        self.sound = sound

    def __eq__(self, obj):
        '''
        It compares the two bark sounds
        '''
        if isinstance(obj, Bark):
            return self.sound == obj.sound
        return false
