import tkinter as tk
import main_menu as menu

"""
TODO: TKinter GUI:
        - Start new session, create new file in folder /desktop/autonote/notes1.txt etc.
        - take screenshot button
        - (windows notification)
"""

def main():
    root = tk.Tk()
    app = menu.MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
