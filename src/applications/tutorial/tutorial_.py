import tkinter
from tkinter import messagebox
from tkinter import ttk

class TutorialWindow:
    def __init__(self, app):
        self.app = app
        self.notebook_frame = tkinter.Frame(self.app)
        self.notebook_frame.pack(fill="both", expand=1)

        # create an instance of the Notebook
        self.notebook = ttk.Notebook()

        # different pages
        self.frame0 = ttk.Frame(self.notebook)
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)
        self.frame4 = ttk.Frame(self.notebook)

        # add the pages
        self.notebook.add(self.frame0, text="Tutorial")
        self.notebook.add(self.frame1, text="Step 1")
        self.notebook.add(self.frame2, text="Step 2")
        self.notebook.add(self.frame3, text="Step 3")
        self.notebook.add(self.frame4, text="Step 4")


class Notebook2:
    def __init__(self, parent):
        self.parent = parent
        self.top_frame = tkinter.Frame(parent, side="top", fill="x")
        self.bottom_frame = tkinter.Frame(parent, side="top", fill="x")

        # top frame attributes
        self.step1_lbl = tkinter.Label(self.top_frame, text="1.Open Inspect Element via the keyboard shortcut: 'F12' or"
                                                            "'Ctrl + Shift + I'")

        # bottom frame attributes
        self.step2_lbl = tkinter.Label(self.bottom_frame, text="2.Locate the 'Elements' tab at the top of the sidebar"
                                                               "window")
        self.bottom_img_frame = tkinter.Frame(self.bottom_frame, side="bottom")








