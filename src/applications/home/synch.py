import webbrowser
import tkinter
from tkinter import messagebox
import configparser
import clipboard
from bs4 import BeautifulSoup
from src.applications.tutorial import tutorial_ as tutorial
import sys


def get_root():
    for path in sys.path:
        if path[len(path) - 6:] == "K-Nect":
            return path


root_path = get_root()


def launch():
    """
    Sync contact algorithm launched when called as a command by the home application. The algorithm requests that the
    user copy HTML code from the 'Connections' page on linkedIN. Once the user confirms they have copied the HTML, the
    contents are copied from the clipboard and examined. If the necessary HTML is included, the sync algorithm is called
    to parse the HTML content

    :return:
    """

    # check if the tutorial window is disabled
    config = configparser.ConfigParser()
    config.read(root_path + r"\config.ini")

    # if the user has not chosen to hide the tutorial window
    if config["SETTINGS"]["tutorial_window"] == "active":
        tutorial.main()
        print("Hello World")

    else:
        webbrowser.open("https://www.linkedin.com/mynetwork/invite-connect/connections/")


if __name__ == '__main__':
    launch()
