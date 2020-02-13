import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3 as sql
import os
from tkinter.font import Font

class MainWindow:
    def __init__(self, MainApp):  # MainApp parameter will be passed as the window for the class
        self.MainApp = MainApp  # Create an instance attribute of the parameter
        self.MainApp.title("Client Timetable")
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

        self.NewRecordButton = tk.Button(self.BottomFrame, text="New Contact", width=12)
        self.NewRecordButton.grid(row=0, padx=50, pady=8)

        self.ViewContactsButton = tk.Button(self.BottomFrame, text="View Contacts", width=12)
        self.ViewContactsButton.grid(column=2, row=0, padx=50, pady=8)

        self.DeleteRecordButton = tk.Button(self.BottomFrame, text="Delete Contact", width=12)
        self.DeleteRecordButton.grid(row=1, padx=50, pady=8)

        self.LogoutButton = tk.Button(self.BottomFrame, text="Logout", width=12)
        self.LogoutButton.grid(column=2, row=1, pady=8)

def main():
    main_window_app = tk.Tk()
    MainWindow(main_window_app)
    main_window_app.mainloop()

if __name__ == "__main__":
    main()




        #if DoesFileExist("Current Database.txt"):
            #self.UpdateListbox()  # calls the class method which updates the listbox in the main window

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
    #
    # def LoadNewClientWindow(self):  # loads the new client window by creating an object of the class which inherits the main application as a parent window
    #     self.ClientApp = tk.Toplevel(self.MainApp)  # TopLevel is a child window of whatever window passed as arg
    #     self.ClientWindow = NewClientWindow(self.ClientApp)  # NewClientWindow class inherits the toplevel window of the main application
    #
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
