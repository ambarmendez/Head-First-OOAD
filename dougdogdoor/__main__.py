'''
It simulates what happens on the alternate path
'''
import time

from .bark import Bark
from .barkrecognizer import BarkRecognizer
from .dogdoor import DogDoor
from .remote import Remote


door = DogDoor(Bark('Woof'))
recognizer = BarkRecognizer(door)
remote = Remote(door)

# Simulate the hardware hearing a bark
print('Bruce starts barking.')
recognizer.recognize(Bark('Woof'))

print('\nBruce has gone outside...')
print("\nBruce's all done...")

t = 10
while t:
    time.sleep(1)
    t -= 1

print("...but he's stuck outside!")

# Simulate the hardware hearing a bark again
print('\nBruce starts barking...')
recognizer.recognize(Bark('Woof'))

print("\nBruce's back inside...")
