import tkinter
from tkinter import ttk
import configparser
import os

assets_path = os.getcwd() + r"\assets"
root_path = assets_path[:50]


def update_config():
    """
    Updates the 'tutorial_window' option in the 'SETTINGS' section to 'disabled' when a user selects the checkbox

    :return:
    """
    config = configparser.ConfigParser()
    config.read(root_path + r"\config.ini")

    config.set("SETTINGS", "tutorial_window", "disabled")
    with open(root_path + r"\config.ini", 'w') as cf:
        config.write(cf)


class TutorialWindow:
    def __init__(self, app):
        self.app = app
        self.app.title("Synching Tutorial")
        self.checkbox_state = tkinter.IntVar()
        self.checkbox = tkinter.Checkbutton(self.app, text="Don't Show this again", variable=self.checkbox_state)

        self.notebook_frame = tkinter.Frame(self.app, bg="white")

        # create an instance of the Notebook
        self.notebook = ttk.Notebook()

        # ttk Frame style
        self.style = ttk.Style()
        self.style.configure("new.TFrame", background="#FFFFFF")

        # different pages
        self.frame1 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame2 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame3 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame4 = ttk.Frame(self.notebook, style="new.TFrame")
        self.frame5 = ttk.Frame(self.notebook, style="new.TFrame")

        # add the pages
        self.notebook.add(self.frame1, text="Tutorial")
        self.notebook.add(self.frame2, text="Step 1")
        self.notebook.add(self.frame3, text="Step 2")
        self.notebook.add(self.frame4, text="Step 3")
        self.notebook.add(self.frame5, text="Step 4")

        # packing
        self.notebook_frame.pack(fill="both", expand=1)
        self.notebook.pack()
        self.checkbox.pack(side="top")

        # instantiate notebook apps
        self.notebook2 = NoteBook2(self.frame2)
        self.notebook3 = NoteBook3(self.frame3)
        self.notebook4 = NoteBook4(self.frame4)
        self.notebook5 = NoteBook5(self.frame5)

        # apply protocol handler to app
        self.app.protocol("WM_DELETE_WINDOW", self.get_checkbox_status)

    def get_checkbox_status(self):
        if self.checkbox_state.get() == 1:
            update_config()
            self.app.withdraw()
        else:
            self.app.withdraw()


class NoteBook2:
    def __init__(self, parent):
        self.parent = parent

        self.top_frame = tkinter.Frame(parent, bg="white")
        self.bottom_frame = tkinter.Frame(parent, bg="white")

        # top frame attributes
        self.step1_lbl = tkinter.Label(self.top_frame, text="1. Open Inspect Element via the keyboard "
                                                            "shortcut:\n'F12' or "
                                                            " 'Ctrl + Shift + I'", bg="white", font=("Arial", 14))

        # bottom frame attributes
        self.step2_lbl = tkinter.Label(self.bottom_frame, text="2. Locate the 'Elements' tab at the top of the "
                                                               "sidebar window", bg="white", font=("Arial", 14))

        self.bottom_img_frame = tkinter.Frame(self.bottom_frame, bg="white")
        self.elements_img = tkinter.PhotoImage(file=assets_path + r"\elements.png")
        self.elements_lbl = tkinter.Label(self.bottom_img_frame, image=self.elements_img)  # label holding image
        self.elements_lbl.image = self.elements_img  # reference to img

        # packing
        self.top_frame.pack(fill="x", pady=10)
        self.bottom_frame.pack(fill="x", pady=120)
        self.step1_lbl.pack()  # top frame
        self.step2_lbl.pack(pady=5)  # bottom frame
        self.bottom_img_frame.pack(side="bottom")  # bottom frame
        self.elements_lbl.pack()  # bottom frame


class NoteBook3:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent, bg="white")

        self.step3_lbl = tkinter.Label(self.frame, text="1. If not there already, scroll to the top of the window\n "
                                                        "and "
                                                        "locate the code that looks identical to\n the following "
                                                        "screenshot", bg="white", font=("Arial", 14))
        self.code_img = tkinter.PhotoImage(file=assets_path + r"\code.png")
        self.code_lbl = tkinter.Label(self.frame, image=self.code_img)
        self.code_lbl.image = self.code_img

        # packing
        self.frame.pack(fill=tkinter.BOTH)
        self.step3_lbl.pack(pady=5)
        self.code_lbl.pack()


class NoteBook4:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(parent, bg="white")

        self.step4_lbl = tkinter.Label(self.frame, text="1. Use your mouse to Right Click onto the code and "
                                                        "locate the 'Copy' section.", bg="white", font=("Arial", 14))
        self.step5_lbl = tkinter.Label(self.frame, text="2. Inside the 'Copy' dropdown menu contains the option "
                                                        "'Copy Element'. Click that option to copy the website text",
                                       bg="white", font=("Arial", 14))
        self.element_img = tkinter.PhotoImage(file=assets_path + r"\copy_element.png")
        self.element_lbl = tkinter.Label(self.frame, image=self.element_img)
        self.element_lbl.image = self.element_img

        # packing
        self.frame.pack()
        self.step4_lbl.pack(pady=5)
        self.step5_lbl.pack(pady=5)
        self.element_lbl.pack()


class NoteBook5:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tkinter.Frame(self.parent, bg="white")

        self.step6_lbl = tkinter.Label(self.frame, text="That's it!", bg="white", font=("Arial", 16))
        self.finish_lbl = tkinter.Label(self.frame, text="Once you have selected 'Copy Element', feel free to close "
                                                         "the browser and return to the application to confirm.",
                                        bg="white", font=("Arial", 14))

        # packing
        self.frame.pack()
        self.step6_lbl.pack(pady=5)
        self.finish_lbl.pack(pady=50)


if __name__ == '__main__':
    main_window = tkinter.Tk()
    TutorialWindow(main_window)
    main_window.mainloop()
