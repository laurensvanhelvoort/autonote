import time

import pyautogui
import pytesseract
from PIL import Image, ImageGrab


def take_screenshot():
    # Windows hotkey for selective manual screenshot
    pyautogui.hotkey('win', 'shift', 's')
    time.sleep(8)
    # return retrieved screenshot from clipboard
    return ImageGrab.grabclipboard()


def extract_text(img):
    img.save('screenshot.png')
    # set path for tesseract library
    pytesseract.pytesseract.tesseract_cmd = (
        r'C:\Users\Gebruiker\AppData\Local\Programs\Tesseract-OCR\tesseract'
    )
    # load saved image and extract text
    text = pytesseract.image_to_string(Image.open('screenshot.png'))
    return text


def write_to_notes(text):
    # write extracted text to .txt file on desktop
    with open(r'C:\Users\Gebruiker\Desktop\notes.txt', 'a') as f:
        f.write(text)


write_to_notes(extract_text(take_screenshot()))
