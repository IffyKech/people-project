import tkinter
from tkinter import messagebox
from tkinter import ttk

class TutorialWindow:
    def __init__(self, app):
        self.app = app
        self.notebook_frame = tkinter.Frame(self.app, bg="white")

        # create an instance of the Notebook
        self.notebook = ttk.Notebook()

        # ttk Frame style
        self.style = ttk.Style()
        self.style.configure("new.TFrame", background="#FFFFFF")

        # different pages
        self.frame0 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame1 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame2 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame3 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame4 = ttk.Frame(self.notebook, style="new.TFrame")

        # add the pages
        self.notebook.add(self.frame0, text="Tutorial")
        self.notebook.add(self.frame1, text="Step 1")
        self.notebook.add(self.frame2, text="Step 2")
        self.notebook.add(self.frame3, text="Step 3")
        self.notebook.add(self.frame4, text="Step 4")

        # packing
        self.notebook_frame.pack(fill="both", expand=1)
        self.notebook.pack()
        self.load_notebook2()


    def load_notebook2(self):
        self.notebook2 = Notebook2(self.frame1)


class NoteBook1:
    def __init__(self):



class Notebook2:
    def __init__(self, parent):
        self.parent = parent
        self.top_frame = tkinter.Frame(parent, bg="white")
        self.bottom_frame = tkinter.Frame(parent, bg="white")

        # top frame attributes
        self.step1_lbl = tkinter.Label(self.top_frame, text="1.Open Inspect Element via the keyboard shortcut: 'F12' or"
                                                            "'Ctrl + Shift + I'", bg="white")

        # bottom frame attributes
        self.step2_lbl = tkinter.Label(self.bottom_frame, text="2.Locate the 'Elements' tab at the top of the sidebar"
                                                               " window", bg="white")

        self.bottom_img_frame = tkinter.Frame(self.bottom_frame, bg="white")
        self.elements_img = tkinter.PhotoImage(file=r"C:\Users\ify_0\Documents\Computing\Projects\K-Nect\src"
                                                    r"\applications\tutorial\assets\elements.png")
        self.elements_lbl = tkinter.Label(self.bottom_img_frame, image=self.elements_img) # label holding image
        self.elements_lbl.image = self.elements_img # reference to img

        # packing
        self.top_frame.pack(side="top", fill="x", pady=10)
        self.bottom_frame.pack(side="bottom", fill="x", pady=10)
        self.step1_lbl.pack() # top frame
        self.step2_lbl.pack(pady=5) # bottom frame
        self.bottom_img_frame.pack(side="bottom") # bottom frame
        self.elements_lbl.pack() # bottom frame



if __name__ == '__main__':
    main_window = tkinter.Tk()
    TutorialWindow(main_window)
    main_window.mainloop()