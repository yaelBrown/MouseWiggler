import time
from pynput.keyboard import Controller, Key

keyboard = Controller()

def press_key():
    while True:
        keyboard.press(Key.space)  # Change this to any key you want
        keyboard.release(Key.space)
        print("Key pressed")
        time.sleep(3)  # Wait for 3 seconds

if __name__ == "__main__":
    press_key()
