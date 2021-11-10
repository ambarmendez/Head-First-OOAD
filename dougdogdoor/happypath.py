if __name__ == '__main__':

    from .dogdoor import DogDoor
    from .remote import Remote


    door = DogDoor()
    remote = Remote(door)

    print('Fido barks to go outside...')
    remote.press_button()

    print('\nFido has gone outside...')
    print("\nFido's all done...")
    print("\nFido's back inside...")
