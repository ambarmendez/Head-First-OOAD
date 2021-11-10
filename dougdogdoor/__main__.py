'''
It simulates what happens on the alternate path
'''
import time

from .dogdoor import DogDoor
from .remote import Remote

door = DogDoor()
remote = Remote(door)

print('Fido barks to go outside...')
remote.press_button()

print('\nFido has gone outside...')
print("\nFido's all done...")

t = 10
while t:
    time.sleep(1)
    t -= 1

print("...but he's stuck outside!")
print('\nFido starts barkig...')

print('...so Gina grabs the remote control.')
remote.press_button()

print("\nFido's back inside...")
