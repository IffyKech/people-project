import tkinter as tk
from src.components import mainwindow
import sqlite3 as sql
import os

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


def main():
    if not doesfileexist("contacts.sqlite3"):
        createdatabase()
    main_window_app = tk.Tk()
    mainwindow.MainWindow(main_window_app)
    main_window_app.mainloop()


if __name__ == "__main__":
    main()
