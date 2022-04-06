import pygetwindow
import time

from buffdetection import find_buff
from window import make_window

TARGET_WINDOW = "RuneScape"

titles = pygetwindow.getAllTitles()

if TARGET_WINDOW not in titles:
    print("Error: Couldn't find RS window")
    exit(-1)

"""
while True:
    if find_buff(TARGET_WINDOW, 0.9, "img/turmoil-cropped.png"):
        print("Buff found!")
    else:
        print("Buff not found.")
    time.sleep(0.6)
"""

def test():
    print("hello!")

if __name__ == "__main__":
    make_window(test)