import pygetwindow

from window import make_window
from constants import TARGET_WINDOW

if __name__ == "__main__":
    titles = pygetwindow.getAllTitles()

    if TARGET_WINDOW not in titles:
        print("Error: Couldn't find RS window")
        exit(-1)

    make_window()