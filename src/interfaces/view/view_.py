import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

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