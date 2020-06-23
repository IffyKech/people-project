import sqlite3 as sql
import tkinter as tk
from tkinter import messagebox, ttk


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