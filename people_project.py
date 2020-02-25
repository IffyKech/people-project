import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3 as sql
import os
from tkinter.font import Font

class MainWindow:
    def __init__(self, MainApp):  # MainApp parameter will be passed as the window for the class
        self.MainApp = MainApp  # Create an instance attribute of the parameter
        self.MainApp.title("Peepl Book")
        #self.MainApp.geometry("800x500")

        self.TopFrame = tk.Frame(self.MainApp, bg = "white")
        self.TopFrame.pack(side=tk.TOP)

        self.BottomFrame = tk.Frame(self.MainApp, bg="white")
        self.BottomFrame.pack(side=tk.BOTTOM)

        self.ClientText = tk.Label(self.TopFrame, text="Clients", font=("Arial", 14), bg="White")
        self.ClientText.pack()

        self.yscrollbar = tk.Scrollbar(self.TopFrame)
        self.yscrollbar.pack(side=tk.RIGHT,
                                  fill=tk.Y)  # Scrollbar attached to right side of listbox, scrolls down the listbox (vertical)

        self.xscrollbar = tk.Scrollbar(self.TopFrame, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.ClientListbox = tk.Listbox(self.TopFrame, width=45, height=5,
                                        yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)  # sets the scrollbars made above to this listbox
        self.ClientListbox.pack()

        self.yscrollbar.config(
            command=self.ClientListbox.yview)  # yview will scroll down the listbox (vertical) when the scroll slider or button is manipulated
        self.xscrollbar.config(command=self.ClientListbox.xview)

        self.NewRecordButton = tk.Button(self.BottomFrame, text="New Contact", width=12, command=self.load_new_record)
        self.NewRecordButton.grid(row=0, padx=50, pady=8)

        self.ViewContactsButton = tk.Button(self.BottomFrame, text="View Contacts", width=12, command=self.load_view_record)
        self.ViewContactsButton.grid(column=2, row=0, padx=50, pady=8)

        self.DeleteRecordButton = tk.Button(self.BottomFrame, text="Delete Contact", width=12, command=self.load_delete_record)
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
        self.newrecordapp = tk.Toplevel(self.MainApp)
        self.newrecordwindow = NewRecordWindow(self.newrecordapp)

    def load_delete_record(self):
        self.deleterecordapp = tk.Toplevel(self.MainApp)
        self.deleterecordwindow = DeleteRecordWindow(self.deleterecordapp)

    def load_view_record(self):
        self.viewrecordapp = tk.Toplevel(self.MainApp)
        self.viewrecordwindow = ViewRecordWindow(self.viewrecordapp)

    def close_main_window(self):
        self.MainApp.destroy()

class NewRecordWindow:
    def __init__(self, Parent):  # Parent parameter will be passed as the window for the class
        self.Parent = Parent  # Create an instance attribute of the parameter
        self.Parent.title("New Contact")
        self.Parent.geometry("275x460")

        self.Frame = tk.Frame(self.Parent, bg="white")
        self.Frame.pack()

        self.NewClientText = tk.Label(self.Frame, text="Fill in details", font=("Arial 8 bold"), bg="white")
        self.NewClientText.grid(row=0, column=0)

        self.FirstnameText = tk.Label(self.Frame, text="Firstname: ", bg="white")
        self.FirstnameText.grid(pady=12, row=1, column=0)

        self.LastnameText = tk.Label(self.Frame, text="Lastname: ", bg="white")
        self.LastnameText.grid(pady=12, row=2, column=0)

        self.LocationText = tk.Label(self.Frame, text="Location: ", bg="white")
        self.LocationText.grid(pady=12, row=3, column = 0)

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
        self.EmailEntry.grid(row=5, column = 1)

        self.FieldOfWorkEntry = tk.Entry(self.Frame)
        self.FieldOfWorkEntry.grid(row=6, column=1)

        self.SourceEntry = tk.Entry(self.Frame)
        self.SourceEntry.grid(row=7, column=1)

        self.OccupationEntry = tk.Entry(self.Frame)
        self.OccupationEntry.grid(row=8, column=1)

        self.ExistingOccupationDropDown = tk.ttk.Combobox(self.Frame, state="readonly", justify=tk.CENTER)
        self.ExistingOccupationDropDown.grid(row=9, column=1)
        self.ExistingOccupationDropDown.configure(values=("Placeholder", "Placeholder", "Placeholder"))

        self.SaveButton = tk.Button(self.Frame, text="Save/Exit", command = self.addClientToDatabase)
        self.SaveButton.grid(row=10, columnspan=2)

    def addClientToDatabase(self):
        self.occupation = self.ExistingOccupationDropDown.get()
        if len(self.OccupationEntry.get()) > 1:  # if they created a new occupation, take that one instead
            self.occupation = self.OccupationEntry.get()

        if not doesfileexist("contacts.sqlite3"):  # create the database file just in case it doesn't exist
            createdatabase()
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()
        databasecursor.execute("""INSERT INTO Contacts(Firstname, Lastname, Location, Number, Email, FieldOfWork, Source, Occupation)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (self.FirstnameEntry.get(), self.LastnameEntry.get(), self.LocationEntry.get(),
                                            self.NumberEntry.get(), self.EmailEntry.get(), self.FieldOfWorkEntry.get(),
                                            self.SourceEntry.get(), self.occupation))
        database.commit()
        database.close()

        messagebox.showinfo(title="Record Created", message="Record added to database")
        self.Parent.withdraw()

class DeleteRecordWindow:
    def __init__(self, Parent):
        self.parent = Parent
        self.parent.geometry("240x69")
        self.parent.title("Delete Record")

        self.Frame = tk.Frame(self.parent, bg="white")
        self.Frame.pack()

        self.DeleteRecordText = tk.Label(self.Frame, text="Select which record you would like to delete", bg="white")
        self.DeleteRecordText.pack()

        self.RecordCombobox = ttk.Combobox(self.Frame, state="readonly", justify=tk.CENTER)
        self.RecordCombobox.configure(values=(self.getrecords()))
        self.RecordCombobox.pack()

        self.DeleteButton = tk.Button(self.Frame, text="Delete", command=self.deleterecord)
        self.DeleteButton.pack()

    def getrecords(self):
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()
        records = [row[0] for row in databasecursor.execute('SELECT Firstname FROM Contacts')]
        database.close()

        return records

    def deleterecord(self):
        recordtodelete = self.RecordCombobox.get()
        if messagebox.askyesno(title="Confirm Deletion", message="Are you sure you want to delete %s?" % (recordtodelete)):
            database = sql.connect("contacts.sqlite3")
            databasecursor = database.cursor()
            databasecursor.execute("""DELETE FROM Contacts WHERE Firstname = ?""", (recordtodelete,))
            database.commit()
            database.close()

            messagebox.showinfo(title="Deleted Record", message="%s deleted from database" % (recordtodelete))
            self.parent.destroy()

class ViewRecordWindow:
    def __init__(self, Parent):
        self.parent = Parent
        self.parent.title("Records")

        self.Frame = tk.Frame(self.parent)
        self.Frame.pack(fill=tk.BOTH, expand=tk.Y)

        self.sortingframe = tk.Frame(self.Frame)
        self.sortingframe.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.sortingframe, text="Test", bg="red").pack(fill=tk.X)

        self.create_tree_window()

    def create_tree_window(self):
        self.treeframe = tk.Frame(self.Frame)
        self.treeframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.Y)

        # creating the columns(fields) for records
        self.tree = ttk.Treeview(self.treeframe)
        self.tree["columns"] = ("Source", "Firstname", "Lastname", "FieldOfWork", "Occupation", "Location", "Telephone", "Email")
        self.tree["show"] = "headings"  # hides the extra first column that was appearing
        self.tree.column("Source", anchor=tk.CENTER, stretch=True)  # first param is the column to edit
        self.tree.column("Firstname", anchor=tk.CENTER, stretch=True)
        self.tree.column("Lastname", anchor=tk.CENTER, stretch=True)
        self.tree.column("FieldOfWork", anchor=tk.CENTER, stretch=True)
        self.tree.column("Occupation", anchor=tk.CENTER, stretch=True)
        self.tree.column("Location", anchor=tk.CENTER, stretch=True)
        self.tree.column("Telephone", anchor=tk.CENTER, stretch=True)
        self.tree.column("Email", anchor=tk.CENTER, stretch=True)

        # creating the headings(titles) of the columns(/fields)
        self.tree.heading("Source", text="Source", anchor=tk.CENTER)
        self.tree.heading("Firstname", text="Firstname", anchor=tk.CENTER)
        self.tree.heading("Lastname", text="Lastname", anchor=tk.CENTER)
        self.tree.heading("FieldOfWork", text="Field Of Work", anchor=tk.CENTER)
        self.tree.heading("Occupation", text="Occupation", anchor=tk.CENTER)
        self.tree.heading("Location", text="Location", anchor=tk.CENTER)
        self.tree.heading("Telephone", text="Telephone", anchor=tk.CENTER)
        self.tree.heading("Email", text="Email", anchor=tk.CENTER)

        self.tree.pack()

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
    MainWindow(main_window_app)
    main_window_app.mainloop()

if __name__ == "__main__":
    main()





