import tkinter as tk
import sqlite3 as sql
from src.applications.delete import delete_ as delete
from src.applications.new import new_ as new
from src.applications.view import view_ as view
from src.applications.home import synch

class MainWindow:
    def __init__(self, main_app):  # main_app parameter will be passed as the window for the class
        self.main_app = main_app  # Create an instance attribute of the parameter
        self.main_app.title("K-Nect")

        self.TopFrame = tk.Frame(self.main_app, bg="white")
        self.TopFrame.pack(side=tk.TOP)

        self.BottomFrame = tk.Frame(self.main_app, bg="white")
        self.BottomFrame.pack(side=tk.BOTTOM)

        self.ClientText = tk.Label(self.TopFrame, text="Clients", font=("Arial", 14), bg="White")
        self.ClientText.pack()

        self.yscrollbar = tk.Scrollbar(self.TopFrame)
        self.yscrollbar.pack(side=tk.RIGHT,
                             fill=tk.Y)  # Scrollbar attached to right side of listbox, scrolls down the listbox (
        # vertical)

        self.xscrollbar = tk.Scrollbar(self.TopFrame, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.ClientListbox = tk.Listbox(self.TopFrame, width=45, height=5,
                                        yscrollcommand=self.yscrollbar.set,
                                        xscrollcommand=self.xscrollbar.set)  # sets the scrollbars made above to this
        # listbox
        self.ClientListbox.pack()

        self.yscrollbar.config(
            command=self.ClientListbox.yview)  # yview will scroll down the listbox (vertical) when the scroll slider
        # or button is manipulated
        self.xscrollbar.config(command=self.ClientListbox.xview)

        self.NewRecordButton = tk.Button(self.BottomFrame, text="New Contact", width=12, command=self.load_new_record)
        self.NewRecordButton.grid(row=0, padx=50, pady=8)

        self.ViewContactsButton = tk.Button(self.BottomFrame, text="View Contacts", width=12,
                                            command=self.load_view_record)
        self.ViewContactsButton.grid(column=2, row=0, padx=50, pady=8)

        self.DeleteRecordButton = tk.Button(self.BottomFrame, text="Delete Contact", width=12,
                                            command=self.load_delete_record)
        self.DeleteRecordButton.grid(row=1, padx=50, pady=8)

        self.LogoutButton = tk.Button(self.BottomFrame, text="Logout", width=12, command=self.close_main_window)
        self.LogoutButton.grid(column=2, row=1, pady=8)

        if doesfileexist("contacts.sqlite3"):
            self.updatelistbox()

    def updatelistbox(self):
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()

        querystatement = """SELECT Firstname, Lastname, Number, Email, Location, Occupation FROM Contacts"""

        databasecursor.execute(querystatement)

        records = [row for row in databasecursor]

        database.close()

        for record in records:
            self.ClientListbox.insert(tk.END, record)

    def load_new_record(self):
        self.newrecordapp = tk.Toplevel(self.main_app)
        self.newrecordwindow = new.NewRecordWindow(self.newrecordapp)

    def load_delete_record(self):
        self.deleterecordapp = tk.Toplevel(self.main_app)
        self.deleterecordwindow = delete.DeleteRecordWindow(self.deleterecordapp)

    def load_view_record(self):
        self.viewrecordapp = tk.Toplevel(self.main_app)
        self.viewrecordwindow = view.ViewRecordWindow(self.viewrecordapp)

    def close_main_window(self):
        self.main_app.destroy()


def doesfileexist(filetofind):
    import os
    for file in os.listdir():
        if filetofind == file:
            return True
    return False


def createdatabase():
    database = sql.connect("contacts.sqlite3")

    databasecursor = database.cursor()
    databasecursor.execute("""CREATE TABLE Contacts(Firstname TEXT, Lastname TEXT, Location TEXT, Number TEXT,
     Email TEXT, FieldOfWork TEXT, Source TEXT, Occupation TEXT)""")

    database.commit()
    database.close()


def main():
    try:
        main_window = tk.Tk()
        MainWindow(main_window)
        main_window.mainloop()

    except Exception as err:
        print(err)
        input()


if __name__ == "__main__":
    main()
