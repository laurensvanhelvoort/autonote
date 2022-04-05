import time
import tkinter as tk
from tkinter import *

import pyautogui
import pytesseract
from PIL import Image, ImageGrab

"""
TODO: TKinter GUI:
        - Start new session, create new file in folder /desktop/autonote/notes1.txt etc.
        - take screenshot button
    
    Layout:
        - welcome window
            - start new session > new file
            - continue previous session
            - open notes
        - note window
            - image button with take screenshot
            - quit session
"""


class MainApplication(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.master.geometry('275x75')
        self.master.resizable(False, False)
        self.master.title('Autonote')
        autonote_icon = PhotoImage(file=r'assets\autonote_icon.png')
        self.master.iconphoto(True, autonote_icon)

        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=BOTH, expand=True)

        self.screenshot_icon = PhotoImage(file=r'assets\screenshot.png')
        self.autonote_btn = tk.Button(self.frame,
                                      command=lambda: self.write_to_notes(self.extract_text(self.take_screenshot())),
                                      image=self.screenshot_icon)
        self.autonote_btn.pack(side=LEFT, expand=True, fill=BOTH)

        self.quit_icon = PhotoImage(file=r'assets\quit.png')
        self.quit_btn = tk.Button(self.frame, command=lambda: self.master.destroy(), image=self.quit_icon)
        self.quit_btn.pack(side=RIGHT, expand=True, fill=BOTH)

    @staticmethod
    def take_screenshot():
        time.sleep(1)
        # Windows hotkey for selective manual screenshot
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(8)
        # return retrieved screenshot from clipboard
        return ImageGrab.grabclipboard()

    @staticmethod
    def extract_text(img):
        img.save('screenshot.png')
        # set path for tesseract library
        pytesseract.pytesseract.tesseract_cmd = (
            r'C:\Users\Gebruiker\AppData\Local\Programs\Tesseract-OCR\tesseract'
        )
        # load saved image and extract text
        text = pytesseract.image_to_string(Image.open('screenshot.png'))
        return text

    @staticmethod
    def write_to_notes(text):
        # write extracted text to .txt file on desktop
        with open(r'C:\Users\Gebruiker\Desktop\notes.txt', 'a') as f:
            f.write(text + "\n\n")
            print(f"'{text}' written.")


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.mainloop()


if __name__ == '__main__':
    main()
