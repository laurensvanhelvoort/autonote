import tkinter as tk
import main_menu as menu


def main():
    root = tk.Tk()
    app = menu.MainMenu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
