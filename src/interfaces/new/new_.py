import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox

class NewRecordWindow:
    def __init__(self, Parent):  # Parent parameter will be passed as the window for the class
        self.Parent = Parent  # Create an instance attribute of the parameter
        self.Parent.title("New Contact")
        self.Parent.geometry("275x460")

        self.Frame = tk.Frame(self.Parent, bg="white")
        self.Frame.pack()

        if not doesfileexist("contacts.sqlite3"):  # create the database file just in case it doesn't exist
            createdatabase()

        self.NewClientText = tk.Label(self.Frame, text="Fill in details", font="Arial 8 bold", bg="white")
        self.NewClientText.grid(row=0, column=0)

        self.FirstnameText = tk.Label(self.Frame, text="Firstname: ", bg="white")
        self.FirstnameText.grid(pady=12, row=1, column=0)

        self.LastnameText = tk.Label(self.Frame, text="Lastname: ", bg="white")
        self.LastnameText.grid(pady=12, row=2, column=0)

        self.LocationText = tk.Label(self.Frame, text="Location: ", bg="white")
        self.LocationText.grid(pady=12, row=3, column=0)

        self.NumberText = tk.Label(self.Frame, text="Phone: ", bg="white")
        self.NumberText.grid(pady=12, row=4, column=0)

        self.EmailText = tk.Label(self.Frame, text="Email: ", bg="white")
        self.EmailText.grid(pady=12, row=5, column=0)

        self.FieldOfWorkText = tk.Label(self.Frame, text="Field of Work: ", bg="white")
        self.FieldOfWorkText.grid(pady=12, row=6, column=0)

        self.SourceText = tk.Label(self.Frame, text="Source: ", bg="white")
        self.SourceText.grid(pady=12, row=7, column=0)

        self.NewOccupationText = tk.Label(self.Frame, text="New Occupation: ", bg="white")
        self.NewOccupationText.grid(pady=12, row=8, column=0)

        self.ExistingOccupationText = tk.Label(self.Frame, text="Existing Occupations: ", bg="white")
        self.ExistingOccupationText.grid(pady=12, row=9, column=0)

        self.FirstnameEntry = tk.Entry(self.Frame)
        self.FirstnameEntry.grid(row=1, column=1)

        self.LastnameEntry = tk.Entry(self.Frame)
        self.LastnameEntry.grid(row=2, column=1)

        self.LocationEntry = tk.Entry(self.Frame)
        self.LocationEntry.grid(row=3, column=1)

        self.NumberEntry = tk.Entry(self.Frame)
        self.NumberEntry.grid(row=4, column=1)

        self.EmailEntry = tk.Entry(self.Frame)
        self.EmailEntry.grid(row=5, column=1)

        self.FieldOfWorkEntry = tk.Entry(self.Frame)
        self.FieldOfWorkEntry.grid(row=6, column=1)

        self.SourceEntry = tk.Entry(self.Frame)
        self.SourceEntry.grid(row=7, column=1)

        self.OccupationEntry = tk.Entry(self.Frame)
        self.OccupationEntry.grid(row=8, column=1)

        self.ExistingOccupations = self.getOccupations()
        self.ExistingOccupationDropDown = tk.ttk.Combobox(self.Frame, state="readonly", justify=tk.CENTER)
        self.ExistingOccupationDropDown.grid(row=9, column=1)
        self.ExistingOccupationDropDown.configure(values=self.ExistingOccupations)

        self.SaveButton = tk.Button(self.Frame, text="Save/Exit", command=self.addClientToDatabase)
        self.SaveButton.grid(row=10, columnspan=2)

    def getOccupations(self):
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()

        querystatement = """SELECT Occupation FROM Contacts"""

        occupations = []
        for row in databasecursor.execute(querystatement):
            if row not in occupations:
                occupations.append(row)

        database.close()

        return occupations

    def addClientToDatabase(self):
        self.occupation = self.ExistingOccupationDropDown.get()
        if len(self.OccupationEntry.get()) > 1:  # if they created a new occupation, take that one instead
            self.occupation = self.OccupationEntry.get()

        self.occupation = self.occupation.replace(" ", "_")
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()
        databasecursor.execute("""INSERT INTO Contacts(Firstname, Lastname, Location, Number, Email, FieldOfWork,
         Source, Occupation) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                               (self.FirstnameEntry.get(), self.LastnameEntry.get(), self.LocationEntry.get(),
                                self.NumberEntry.get(), self.EmailEntry.get(), self.FieldOfWorkEntry.get(),
                                self.SourceEntry.get(), self.occupation))
        database.commit()
        database.close()

        messagebox.showinfo(title="Record Created", message="Record added to database")
        self.Parent.withdraw()


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
