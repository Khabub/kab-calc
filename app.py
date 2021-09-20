import tkinter as tk
from tkinter import ttk
import tkinter.font as font


RED = "red"
BLACK = "black"

calc = [
    {"C": (1, BLACK), "NA1": (1, BLACK), "NA2": (1, BLACK), "DEL": (1, BLACK)},
    {"7": (1, BLACK), "8": (1, BLACK), "9": (1, BLACK), "/": (1, BLACK)},
    {"4": (1, BLACK), "5": (1, BLACK), "6": (1, BLACK), "*": (1, BLACK)},
    {"1": (1, BLACK), "2": (1, BLACK), "3": (1, BLACK), "-": (1, BLACK)},
    {"0": (1, BLACK), ".": (1, BLACK), "=": (1, RED), "+": (1, BLACK)}
]


class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kabub Calculator")
        self.geometry("330x480+1000+800")
        #self.resizable(False, False)


        self.val = tk.IntVar()


        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")


        display = ttk.Label(container, text="Testik", font=("Segoe UI", 40), textvariable=self.val)
        display.grid(row=0, column=0, sticky="ne", padx=15, pady=20)



        keypad = ttk.Frame(container)
        keypad.grid(row=1, column=0, sticky="swe", padx=10, pady=10)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        row = 0
        for rows in calc:
            col = 0
            for key, value in rows.items():
                button = tk.Button(
                    keypad,
                    text=key,
                    height=1,
                    width=4,
                    font=("Segoe UI bold", 20),
                    foreground=value[1],
                    command=self.addval(value[0])
                )
                button.grid(row=row, column=col, columnspan=value[0], padx=2, pady=2)
                col += value[0]
            row += 1

        but = ttk.Button(container, command=self.addval)
        but.grid(row=2, column=1)

    def addval(self, v):

        self.val.set(v)


root = Calculator()

#font.nametofont("TkDefaultFont").configure(size=15)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()
