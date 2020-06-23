import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox, ttk
import os
import webbrowser
from src.server import app



import requests
# import time


# TODO: CREATE MORE MODULES (interface, funcs e.t.c) TO CLEAN UP CODE
class MainWindow:
    def __init__(self, MainApp):  # MainApp parameter will be passed as the window for the class
        self.MainApp = MainApp  # Create an instance attribute of the parameter
        self.MainApp.title("Peepl Book")

        self.TopFrame = tk.Frame(self.MainApp, bg="white")
        self.TopFrame.pack(side=tk.TOP)

        self.BottomFrame = tk.Frame(self.MainApp, bg="white")
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
        self.newrecordapp = tk.Toplevel(self.MainApp)
        self.newrecordwindow = NewRecordWindow(self.newrecordapp)

    def load_delete_record(self):
        self.deleterecordapp = tk.Toplevel(self.MainApp)
        self.deleterecordwindow = DeleteRecordWindow(self.deleterecordapp)

    def load_view_record(self):
        self.viewrecordapp = tk.Toplevel(self.MainApp)
        self.viewrecordwindow = ViewRecordWindow(self.viewrecordapp)

    def close_main_window(self):
        # shutdown the server when the user closes the app
        # shutdown_request = requests.post("http://127.0.0.1:5000/shutdown", data={"null" : "null"})
        self.MainApp.destroy()

    # def linkedIn_login(self):
    # src.people_project.request_auth_code()


class ViewRecordWindow:
    def __init__(self, Parent):
        self.parent = Parent
        self.parent.title("Records")

        self.Frame = tk.Frame(self.parent)
        self.Frame.pack(fill=tk.BOTH, expand=tk.Y)

        self.sortingframe = tk.Frame(self.Frame, bg="white")
        self.sortingframe.pack(side=tk.TOP, fill=tk.X)

        self.sortbytext = tk.Label(self.sortingframe, text="Sort By: ", bg="white")
        self.sortbytext.grid(row=0, column=1)

        # get the occupations which will be added to the combobox
        self.searchfilter = ""
        self.records = []
        self.occupations = []
        self.get_records_occupation(self.searchfilter)
        self.sortingcombobox = ttk.Combobox(self.sortingframe, state="readonly", justify=tk.CENTER)
        self.sortingcombobox.configure(values=self.occupations)
        self.sortingcombobox.grid(row=0, column=2)

        self.sortbutton = tk.Button(self.sortingframe, text="Sort", width=7, height=0, font=('Arial', 8),
                                    command=self.filter_tree_window)
        self.sortbutton.grid(row=0, column=3, padx=10)

        self.create_tree_window(self.Frame)

    def create_tree_window(self, master):
        self.treeframe = tk.Frame(master)
        self.treeframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.Y)

        # creating the columns(fields) for records
        self.tree = ttk.Treeview(self.treeframe)
        self.tree["columns"] = (
            "Source", "Firstname", "Lastname", "FieldOfWork", "Occupation", "Location", "Telephone", "Email")
        self.tree["show"] = "headings"  # hides the extra first column that was appearing
        self.tree.column("Source", anchor=tk.CENTER, width=110)  # first param is the column to edit
        self.tree.column("Firstname", anchor=tk.CENTER, width=110)
        self.tree.column("Lastname", anchor=tk.CENTER, width=110)
        self.tree.column("FieldOfWork", anchor=tk.CENTER, width=120)
        self.tree.column("Occupation", anchor=tk.CENTER, width=120)
        self.tree.column("Location", anchor=tk.CENTER, width=110)
        self.tree.column("Telephone", anchor=tk.CENTER, width=110)
        self.tree.column("Email", anchor=tk.CENTER, width=150)

        # creating the headings(titles) of the columns(/fields)
        self.tree.heading("Source", text="Source", anchor=tk.CENTER)
        self.tree.heading("Firstname", text="Firstname", anchor=tk.CENTER)
        self.tree.heading("Lastname", text="Lastname", anchor=tk.CENTER)
        self.tree.heading("FieldOfWork", text="Field Of Work", anchor=tk.CENTER)
        self.tree.heading("Occupation", text="Occupation", anchor=tk.CENTER)
        self.tree.heading("Location", text="Location", anchor=tk.CENTER)
        self.tree.heading("Telephone", text="Telephone", anchor=tk.CENTER)
        self.tree.heading("Email", text="Email", anchor=tk.CENTER)

        # inserting data in
        for row in self.records:
            self.tree.insert('', 'end', values=row)

        # scrollbar adding
        self.yscrollbar = tk.Scrollbar(self.treeframe, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree['yscroll'] = self.yscrollbar.set
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.pack()

    def get_records_occupation(self, searchfilter):  # returns the list of records as a whole and also occupations
        database = sql.connect("contacts.sqlite3")
        databasecursor = database.cursor()
        if searchfilter == "":
            records = [row for row in
                       databasecursor.execute('SELECT Source, Firstname, Lastname, FieldOfWork, Occupation,'
                                              'Location, Number, Email '
                                              'FROM Contacts')]
        else:
            records = [row for row in
                       databasecursor.execute('SELECT Source, Firstname, Lastname, FieldOfWork, Occupation,'
                                              'Location, Number, Email '
                                              'FROM Contacts '
                                              'WHERE Occupation = ?', (searchfilter,))]
        database.close()

        occupations = []
        for row in records:
            if row[4] not in occupations:
                occupations.append(row[4])

        self.records, self.occupations = records, occupations

    def filter_tree_window(self):
        self.searchfilter = self.sortingcombobox.get()
        if self.searchfilter == "":
            messagebox.showinfo(title="Error", message="Please create a new record first")
        else:
            self.get_records_occupation(self.searchfilter)
            filterwindow = tk.Toplevel(self.parent)
            filterwindow.title("%ss" % self.searchfilter)
            self.create_tree_window(filterwindow)


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
        if recordtodelete == "":
            messagebox.showinfo(title="Error", message="Please select a record to delete")
        else:
            if messagebox.askyesno(title="Confirm Deletion",
                                   message="Are you sure you want to delete %s?" % recordtodelete):
                database = sql.connect("contacts.sqlite3")
                databasecursor = database.cursor()
                databasecursor.execute("""DELETE FROM Contacts WHERE Firstname = ?""", (recordtodelete,))
                database.commit()
                database.close()

                messagebox.showinfo(title="Deleted Record", message="%s deleted from database" % recordtodelete)
                self.parent.destroy()


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


def read_secrets():
    with open("src/secrets.txt", 'r') as f:
        client_id = f.readline().strip("\n")
        client_secret = f.readline()
        return client_id, client_secret


def request_auth_code():
    client_id, client_secret = read_secrets()
    redirect_uri = "http://127.0.0.1:5000/callback"
    webbrowser.open("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}"
                    "&redirect_uri={}&state=97b2ff2e09&scope=r_liteprofile"
                    "%20r_emailaddress".format(client_id, redirect_uri), 1)


# def linkedinLogin():
#     """
#     Open the authentication page, then start the web server. Waits for the user to authenticate, then processes the
#     authentication in the webserver. Once complete, the server is shutdown and tk window is run.
#
#     :return:
#     """
#     request_auth_code()
#     app.app.run()
#     # wait for authentication
#     page_response = ""
#     while len(page_response) < 1:





def main():
    try:
        request_auth_code()
        app.app.run()
        main_window = tk.Tk()
        MainWindow(main_window)
        main_window.mainloop()

    except Exception as err:
        print(err)
        input()



if __name__ == "__main__":
    main()

