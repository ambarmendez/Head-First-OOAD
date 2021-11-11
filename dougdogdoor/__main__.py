'''
It simulates what happens on the alternate path
'''
import time

from .bark import Bark
from .barkrecognizer import BarkRecognizer
from .dogdoor import DogDoor
from .remote import Remote


door = DogDoor()
door.add_allowed_bark(Bark('rowlf'))
door.add_allowed_bark(Bark('rooowlf'))
door.add_allowed_bark(Bark('rawlf'))
door.add_allowed_bark(Bark('woof'))

recognizer = BarkRecognizer(door)
remote = Remote(door)

# Simulate the hardware hearing a bark
print('Bruce starts barking.')
recognizer.recognize(Bark('rowlf'))

print('\nBruce has gone outside...')

t = 10
while t:
    time.sleep(1)
    t -= 1

print("\nBruce's all done...")
print("...but he's stuck outside!")

# Simulate the hardware hearing a bark (not Bruce!)
small_dog_bark = Bark('yip')
print('Bitsie dog starts barking.')
recognizer.recognize(small_dog_bark)

t = 5
while t:
    time.sleep(1)
    t -= 1

# Simulate the hardware hearing a bark again
print('Bruce starts barking...')
recognizer.recognize(Bark('rooowlf'))

print("\nBruce's back inside...")
