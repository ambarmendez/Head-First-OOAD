'''
It simulates what happens on the alternate path
'''
import time

from .barkrecognizer import BarkRecognizer
from .dogdoor import DogDoor
from .remote import Remote

door = DogDoor()
recognizer = BarkRecognizer(door)
remote = Remote(door)

# Simulate the hardware hearing a bark
print('Fido starts barking.')
recognizer.recognize('Woof')

print('\nFido has gone outside...')
print("\nFido's all done...")

t = 10
while t:
    time.sleep(1)
    t -= 1

print("...but he's stuck outside!")

# Simulate the hardware hearing a bark again
print('Fido starts barkig...')
recognizer.recognize('Woof')

print("\nFido's back inside...")
