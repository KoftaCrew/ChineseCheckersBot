import tkinter as tk

from checker_frame import CheckerFrame

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Chinese Checker")

    window.minsize(800, 600)

    checkers = CheckerFrame(window, background="white")
    checkers.pack(fill=tk.BOTH, expand=True)

    window.mainloop()
