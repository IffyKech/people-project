import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3 as sql
import os
from tkinter.font import Font

class MainWindow:
    def __init__(self, MainApp):  # MainApp parameter will be passed as the window for the class
        self.MainApp = MainApp  # Create an instance attribute of the parameter
        self.MainApp.title("Client Timetable")

        self.TopFrame = tk.Frame(self.MainApp, bg = "white")
        self.TopFrame.pack()

        self.BottomFrame = tk.Frame(self.MainApp, bg="white")
        self.BottomFrame.pack(side=tk.BOTTOM)

        self.NewClientButton = tk.Button(self.BottomFrame, text="New Client", width=12, command=self.LoadNewClientWindow)  # activates method which loads the request form
        self.NewClientButton.grid(row=0)

        self.DeleteClientButton = tk.Button(self.BottomFrame, text="Delete Client", width=12, command=self.LoadDeleteClientWindow)
        self.DeleteClientButton.grid(row=1, padx=50)

        self.CreateDatabaseButton = tk.Button(self.BottomFrame, text="Create Database", width=12, command=self.LoadNewDatabaseWindow)
        self.CreateDatabaseButton.grid(row=0, column=2, padx=50, pady=3)

        self.ViewDatabaseButton = tk.Button(self.BottomFrame, text="View Database", width=12, command=self.LoadQueryDatabaseWindow)
        self.ViewDatabaseButton.grid(row=1, column=2, padx=50, pady=3)

        self.HelpButton = tk.Button(self.BottomFrame, text="Help", width=12, command = Help)
        self.HelpButton.grid(row=2, padx=50)

        self.LogoutButton = tk.Button(self.BottomFrame, text="Logout", width=12, command= self.CloseMainWindow)
        self.LogoutButton.grid(row=2, column=2, padx=50, pady=3)

        self.SendInvoiceButton = tk.Button(self.BottomFrame, text="Send Invoice", width=12,
                                           command=self.LoadSendInvoiceWindow)
        self.SendInvoiceButton.grid(row=3, columnspan=2, padx=50, pady=3)

        self.ClientText = tk.Label(self.TopFrame, text="Clients", font=("Arial", 14), bg="White")
        self.ClientText.pack()

        self.ClientScrollbar = tk.Scrollbar(self.TopFrame)
        self.ClientScrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Scrollbar attached to right side of listbox, scrolls down the listbox (vertical)

        self.ClientListbox = tk.Listbox(self.TopFrame, width=45, height=5, yscrollcommand=self.ClientScrollbar.set)  # sets the scrollbar made above to this listbox
        self.ClientListbox.pack()

        self.ClientScrollbar.config(command=self.ClientListbox.yview)  # yview will scroll down the listbox (vertical) when the scroll slider or button is manipulated

        if DoesFileExist("Current Database.txt"):
            self.UpdateListbox()  # calls the class method which updates the listbox in the main window

    def UpdateListbox(self):  # queries fields from current database and adds them to a listbox
        DatabaseFile = GetCurrentDatabase()

        QueryStatement = """SELECT Firstname, Lastname, RepairIssue, SessionDate, SessionTime FROM Clients """  # SQL statement to retrieve these fields from all records which will be added to listbox
        Clients = []
        Database = sql.connect(DatabaseFile)

        Cursor = Database.cursor()  # cursor allows sql statements to be executed when a connection is made
        Cursor.execute(QueryStatement)

        for row in Cursor:  # each record in the query
            Clients.append(row)  # append each record to an array

        Database.close()

        for Client in Clients:
            self.ClientListbox.insert(tk.END, Client)  # inserts each element from the list of clients to the listbox in main window

    def LoadNewClientWindow(self):  # loads the new client window by creating an object of the class which inherits the main application as a parent window
        self.ClientApp = tk.Toplevel(self.MainApp)  # TopLevel is a child window of whatever window passed as arg
        self.ClientWindow = NewClientWindow(self.ClientApp)  # NewClientWindow class inherits the toplevel window of the main application

    def LoadDeleteClientWindow(self):
        self.DeleteClientApp = tk.Toplevel(self.MainApp)  # same principle as ‘LoadNewClientWindow’
        self.EditWindow = DeleteClientWindow(self.DeleteClientApp)

    def LoadNewDatabaseWindow(self):
        self.DatabaseApp = tk.Toplevel(self.MainApp)
        self.NewDBWindow = NewDatabaseWindow(self.DatabaseApp)

    def LoadQueryDatabaseWindow(self):
        self.QueryApp = tk.Toplevel(self.MainApp)
        self.QueryWindow = QueryDatabaseWindow(self.QueryApp)

    def LoadSendInvoiceWindow(self):
        self.InvoiceApp = tk.Toplevel(self.MainApp)
        self.InvoiceWindow = InvoiceEmail(self.InvoiceApp)

    def CloseMainWindow(self):  # Closes main window and launches the login window
        self.MainApp.destroy()  # destroys the Tk() application of the main window
        LoginAppWindow = tk.Tk()
        LoginWindow(LoginAppWindow)  # Login window class inherits Tk application
