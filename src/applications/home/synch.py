import webbrowser
import tkinter
from tkinter import messagebox
import configparser
import clipboard
from bs4 import BeautifulSoup
from src.applications.tutorial import tutorial_ as tutorial


def launch():
    """
    Sync contact algorithm launched when called as a command by the home application. The algorithm requests that the
    user copy HTML code from the 'Connections' page on linkedIN. Once the user confirms they have copied the HTML, the
    contents are copied from the clipboard and examined. If the necessary HTML is included, the sync algorithm is called
    to parse the HTML content

    :return:
    """

    webbrowser.open("https://www.linkedin.com/mynetwork/invite-connect/connections/")

    # check if the tutorial window is disabled
    config = configparser.ConfigParser()
    config.read("config.ini")

    # if the user has not chosen to hide the tutorial window
    if config["SETTINGS"]["tutorial_window"] == "active":
        pass

    else:
        pass


if __name__ == '__main__':
    launch()
