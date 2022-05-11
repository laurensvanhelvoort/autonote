import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
import main_application as app

# color palette
col_red = '#da1f26'
col_light_red = '#d9575b'
col_black = '#252525'
col_dark_grey = '#57585a'
col_light_grey = '#9fa3ac'
col_white = '#ffffff'

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry('840x580')
        self.master.minsize(400, 530)
        self.master.maxsize(0, 640)
        self.master.title('Autonote')
        self.master.config(bg=col_black)
        self.autonote_icon = PhotoImage(file=r'assets\autonote_icon.png')
        self.master.iconphoto(True, self.autonote_icon)

        self.frame = Frame(self.master, bg=col_black)
        self.frame.pack()

        # Header label
        self.header_lbl = Label(self.frame,
                                text=' Autonote ',
                                font=('Bahnschrift', 48),
                                bg=col_black,
                                fg=col_white,
                                justify=LEFT)
        self.header_lbl.pack(anchor=W, pady=35)

        # New session button
        self.new_session_img = PhotoImage(file=r'assets/add.png')
        self.new_session_btn = Button(self.frame,
                                      text=' Start new session ',
                                      font=('Bahnschrift Light', 18),
                                      bg=col_black,
                                      fg=col_light_grey,
                                      image=self.new_session_img,
                                      compound=LEFT,
                                      borderwidth=0,
                                      command=lambda: self.new_session())
        self.new_session_btn.pack(pady=(35, 20))

        # Continue session button
        self.continue_session_img = PhotoImage(file=r'assets/continue.png')
        self.continue_session_btn = Button(self.frame,
                                           text=' Continue session ',
                                           font=('Bahnschrift Light', 18),
                                           bg=col_black,
                                           fg=col_light_grey,
                                           image=self.continue_session_img,
                                           compound=LEFT,
                                           borderwidth=0,
                                           command=lambda: self.continue_session())
        self.continue_session_btn.pack(pady=20)

        # Open notes
        self.open_notes_img = PhotoImage(file=r'assets/open_notes.png')
        self.open_notes_btn = Button(self.frame,
                                     text=' Open notes ',
                                     font=('Bahnschrift Light', 18),
                                     bg=col_black,
                                     fg=col_light_grey,
                                     image=self.open_notes_img,
                                     compound=LEFT,
                                     borderwidth=0,
                                     command=lambda: self.open_notes())
        self.open_notes_btn.pack(pady=20)

        # Quit program button
        self.quit_btn = Button(self.frame,
                               text=' Quit ',
                               font=('Bahnschrift Light', 18),
                               bg=col_black,
                               fg=col_red,
                               activebackground=col_light_red,
                               borderwidth=0,
                               command=lambda: self.quit_program())
        self.quit_btn.pack(pady=10)

    def new_session(self):
        self.master.destroy()
        self.master = Tk()
        self.app = app.MainApplication(self.master, isnewsession=True, s_path=None)
        self.master.mainloop()

    def continue_session(self):
        # File dialog to choose file to write to
        filename = askopenfilename(title='Select notes file',
                                   initialdir='/Notes',
                                   filetypes=[('text files', '*.txt')])
        if not filename:
            tk.messagebox.showerror('No file selected', 'You didn\'t select a file!')
            return

        self.master.destroy()
        self.master = Tk()
        self.app = app.MainApplication(self.master, isnewsession=False, s_path=filename)
        self.master.mainloop()

    def open_notes(self):
        path = 'Notes'
        path = os.path.realpath(path)
        os.startfile(path)

    def quit_program(self):
        answer = tk.messagebox.askyesno('Quit', 'Are you sure you want to quit?')
        self.master.destroy() if answer else self.master.mainloop()
