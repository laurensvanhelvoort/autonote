import os
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import PIL.Image
import pyautogui
import pytesseract
from PIL import ImageGrab

import main_menu as menu

col_red = '#da1f26'
col_light_red = '#d9575b'
col_black = '#252525'
col_dark_grey = '#57585a'
col_light_grey = '#9fa3ac'
col_white = '#ffffff'


class MainApplication(tk.Frame):
    def __init__(self, master, isnewsession, s_path):
        # root window config
        self.master = master
        self.master.geometry('275x75')
        self.master.resizable(False, False)
        self.master.title('Autonote')
        self.autonote_icon = PhotoImage(file=r'assets\autonote_icon.png')
        self.master.iconphoto(True, self.autonote_icon)

        self.frame = Frame(self.master)
        self.frame.pack(fill=BOTH, expand=True)

        self.isnewsession = isnewsession
        self.selected_path = s_path
        self.session_ended = False

        # main autonote and quit buttons
        self.screenshot_icon = PhotoImage(file=r'assets\screenshot.png')
        self.autonote_btn = tk.Button(self.frame,
                                      command=lambda: self.write_to_notes(self.extract_text(self.take_screenshot())),
                                      image=self.screenshot_icon,
                                      bg=col_red,
                                      activebackground=col_light_red,
                                      borderwidth=0)
        self.autonote_btn.pack(side=LEFT, expand=True, fill=BOTH)

        self.quit_icon = PhotoImage(file=r'assets\quit.png')
        self.quit_btn = tk.Button(self.frame,
                                  command=self.end_session,
                                  image=self.quit_icon,
                                  bg=col_dark_grey,
                                  activebackground=col_light_grey,
                                  borderwidth=0)
        self.quit_btn.pack(side=RIGHT, expand=True, fill=BOTH)

    def end_session(self):
        self.session_ended = True
        self.master.destroy()
        self.master = Tk()
        self.app = menu.MainMenu(self.master)
        self.master.mainloop()

    def uniquify(self, path_name):
        # add incrementing affixes to filename
        counter = 1
        filename = path_name

        while os.path.exists(filename.format(counter)):
            if self.isnewsession:
                counter += 1
            else:
                counter = counter

        return filename.format(counter)

    def take_screenshot(self):
        time.sleep(1)
        # Windows hotkey for selective manual screenshot
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(8)
        # return retrieved screenshot from clipboard
        return ImageGrab.grabclipboard()

    def extract_text(self, img):
        if img:
            img.save('screenshot.png')
            # set path for tesseract library
            pytesseract.pytesseract.tesseract_cmd = (
                r'C:\Users\Gebruiker\AppData\Local\Programs\Tesseract-OCR\tesseract'
            )
            # load saved image and extract text
            text = pytesseract.image_to_string(PIL.Image.open('screenshot.png'))
            return text if text else messagebox.showerror('Capture failed',
                                                          'Error: Couldn\'t detect any text in your screenshot!')
        else:
            messagebox.showerror('Capture failed', 'Error: You didn\'t take a screenshot!')

    def write_to_notes(self, text):
        global path
        # write extracted text to .txt file
        if not os.path.exists('Notes'):
            try:
                os.mkdir('Notes')
            except OSError:
                messagebox.showerror('Error', 'Error: Something went wrong when creating directory!')

        if not self.session_ended:
            # increment filename counter if new session
            if self.isnewsession:
                path = self.uniquify('Notes/Notes{}.txt')

            # write to user selected file
            if self.selected_path:
                path = self.selected_path

            # write to same file if in current session
            with open(path, 'a') as f:
                f.write(text + '\n')
        self.isnewsession = False
