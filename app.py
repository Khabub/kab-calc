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

        # Keypad buttons
        button_01 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_01.grid(row=1, column=0, padx=2, pady=2)

        button_02 = tk.Button(
            keypad,
            text="NA",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_02.grid(row=1, column=1, padx=2, pady=2)

        button_03 = tk.Button(
            keypad,
            text="NA",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_03.grid(row=1, column=2, padx=2, pady=2)

        button_04 = tk.Button(
            keypad,
            text="DEL",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_04.grid(row=1, column=3, padx=2, pady=2)

        button_05 = tk.Button(
            keypad,
            text="7",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_05.grid(row=2, column=0, padx=2, pady=2)

        button_06 = tk.Button(
            keypad,
            text="8",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_06.grid(row=2, column=1, padx=2, pady=2)

        button_07 = tk.Button(
            keypad,
            text="9",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_07.grid(row=2, column=2, padx=2, pady=2)

        button_08 = tk.Button(
            keypad,
            text="/",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_08.grid(row=2, column=3, padx=2, pady=2)

        button_09 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_09.grid(row=1, column=0, padx=2, pady=2)

        button_10 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_10.grid(row=1, column=0, padx=2, pady=2)

        button_11 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_11.grid(row=1, column=0, padx=2, pady=2)

        button_12 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_12.grid(row=1, column=0, padx=2, pady=2)

        button_13 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_13.grid(row=1, column=0, padx=2, pady=2)

        button_14 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_14.grid(row=1, column=0, padx=2, pady=2)

        button_15 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_15.grid(row=1, column=0, padx=2, pady=2)

        button_16 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_16.grid(row=1, column=0, padx=2, pady=2)

        button_17 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_17.grid(row=1, column=0, padx=2, pady=2)

        button_18 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_18.grid(row=1, column=0, padx=2, pady=2)

        button_19 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_19.grid(row=1, column=0, padx=2, pady=2)

        button_20 = tk.Button(
            keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,

        )
        button_20.grid(row=1, column=0, padx=2, pady=2)

    def addval(self, v):

        self.val.set(v)


root = Calculator()

#font.nametofont("TkDefaultFont").configure(size=15)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()
