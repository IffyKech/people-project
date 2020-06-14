import tkinter as tk
from src.components import mainwindow
import sqlite3 as sql
import os
import webbrowser
from src import secrets
from src.server import app as server


def createdatabase():
    database = sql.connect("contacts.sqlite3")

    databasecursor = database.cursor()
    databasecursor.execute("""CREATE TABLE Contacts(Firstname TEXT, Lastname TEXT, Location TEXT, Number TEXT,
     Email TEXT, FieldOfWork TEXT, Source TEXT, Occupation TEXT)""")

    database.commit()
    database.close()


def doesfileexist(filetofind):
    for file in os.listdir():
        if filetofind == file:
            return True
    return False


# TODO: GET ACCESS TOKEN IN FLASK SERVER, THEN DO SOME ERROR HANDLING IN FLASK SERVER FOR WHEN AUTHORIZATION IS DENIED
def request_auth_code():
    redirect_uri = "http://127.0.0.1:5000/callback"
    webbrowser.open("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}"
                    "&redirect_uri={}&state=97b2ff2e09&scope=r_liteprofile"
                    "%20r_emailaddress".format(secrets.client_id, redirect_uri), 1)


def main():

    if not doesfileexist("contacts.sqlite3"):
        createdatabase()
    main_window_app = tk.Tk()
    mainwindow.MainWindow(main_window_app)
    #main_window_app.mainloop()
    server.app.run()


if __name__ == "__main__":
    main()
