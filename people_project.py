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

        self.ViewContactsButton = tk.Button(self.BottomFrame, text="View Contacts", width=12)
        self.ViewContactsButton.grid(column=2, row=0, padx=50, pady=8)

        self.DeleteRecordButton = tk.Button(self.BottomFrame, text="Delete Contact", width=12)
        self.DeleteRecordButton.grid(row=1, padx=50, pady=8)

        self.LogoutButton = tk.Button(self.BottomFrame, text="Logout", width=12)
        self.LogoutButton.grid(column=2, row=1, pady=8)

        # if DoesFileExist("Current Database.txt"):
        # self.UpdateListbox()  # calls the class method which updates the listbox in the main window

        # def UpdateListbox(self):  # queries fields from current database and adds them to a listbox
        #     DatabaseFile = GetCurrentDatabase()
        #
        #     QueryStatement = """SELECT Firstname, Lastname, RepairIssue, SessionDate, SessionTime FROM Clients """  # SQL statement to retrieve these fields from all records which will be added to listbox
        #     Clients = []
        #     Database = sql.connect(DatabaseFile)
        #
        #     Cursor = Database.cursor()  # cursor allows sql statements to be executed when a connection is made
        #     Cursor.execute(QueryStatement)
        #
        #     for row in Cursor:  # each record in the query
        #         Clients.append(row)  # append each record to an array
        #
        #     Database.close()
        #
        #     for Client in Clients:
        #         self.ClientListbox.insert(tk.END, Client)  # inserts each element from the list of clients to the listbox in main window
        # def LoadDeleteClientWindow(self):
        #     self.DeleteClientApp = tk.Toplevel(self.MainApp)  # same principle as ‘LoadNewClientWindow’
        #     self.EditWindow = DeleteClientWindow(self.DeleteClientApp)
        #
        # def LoadNewDatabaseWindow(self):
        #     self.DatabaseApp = tk.Toplevel(self.MainApp)
        #     self.NewDBWindow = NewDatabaseWindow(self.DatabaseApp)
        #
        # def LoadQueryDatabaseWindow(self):
        #     self.QueryApp = tk.Toplevel(self.MainApp)
        #     self.QueryWindow = QueryDatabaseWindow(self.QueryApp)
        #
        # def LoadSendInvoiceWindow(self):
        #     self.InvoiceApp = tk.Toplevel(self.MainApp)
        #     self.InvoiceWindow = InvoiceEmail(self.InvoiceApp)
        #
        # def CloseMainWindow(self):  # Closes main window and launches the login window
        #     self.MainApp.destroy()  # destroys the Tk() application of the main window
        #     LoginAppWindow = tk.Tk()
        #     LoginWindow(LoginAppWindow)  # Login window class inherits Tk application

    def load_new_record(self):
        self.newrecordapp = tk.Toplevel(self.MainApp)
        self.newrecordwindow = NewRecordWindow(self.newrecordapp)


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

        self.SaveButton = tk.Button(self.Frame, text="Save/Exit")
        self.SaveButton.grid(row=10, columnspan=2)

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





