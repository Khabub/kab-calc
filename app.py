import tkinter as tk
from tkinter import ttk


RED = "red"
BLACK = "black"


class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kabub Calculator")
        self.geometry("330x480+1000+800")
        self.resizable(False, False)
        self.val = tk.StringVar()
        self.val.set("0")
        self.rovnice = ""

        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        display = ttk.Label(container, font=("Segoe UI bold", 30), textvariable=self.val)

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
            command=lambda: self.clear_num()

        )
        button_01.grid(row=1, column=0, padx=2, pady=2)

        button_02 = tk.Button(
            keypad,
            text="NA",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            cursor="hand2",
            foreground=BLACK,
            # command=lambda: self.addval("")

        )
        button_02.grid(row=1, column=1, padx=2, pady=2)

        button_03 = tk.Button(
            keypad,
            text="NA",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            # command=lambda: self.addval("")
        )
        button_03.grid(row=1, column=2, padx=2, pady=2)

        button_04 = tk.Button(
            keypad,
            text="DEL",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.remove_num()
        )
        button_04.grid(row=1, column=3, padx=2, pady=2)

        button_05 = tk.Button(
            keypad,
            text="7",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("7")
        )
        button_05.grid(row=2, column=0, padx=2, pady=2)

        button_06 = tk.Button(
            keypad,
            text="8",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("8")
        )
        button_06.grid(row=2, column=1, padx=2, pady=2)

        button_07 = tk.Button(
            keypad,
            text="9",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("9")
        )
        button_07.grid(row=2, column=2, padx=2, pady=2)

        button_08 = tk.Button(
            keypad,
            text="/",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("/")
        )
        button_08.grid(row=2, column=3, padx=2, pady=2)

        button_09 = tk.Button(
            keypad,
            text="4",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("4")
        )
        button_09.grid(row=3, column=0, padx=2, pady=2)

        button_10 = tk.Button(
            keypad,
            text="5",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("5")
        )
        button_10.grid(row=3, column=1, padx=2, pady=2)

        button_11 = tk.Button(
            keypad,
            text="6",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("6")
        )
        button_11.grid(row=3, column=2, padx=2, pady=2)

        button_12 = tk.Button(
            keypad,
            text="*",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("*")
        )
        button_12.grid(row=3, column=3, padx=2, pady=2)

        button_13 = tk.Button(
            keypad,
            text="1",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("1")
        )
        button_13.grid(row=4, column=0, padx=2, pady=2)

        button_14 = tk.Button(
            keypad,
            text="2",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("2")
        )
        button_14.grid(row=4, column=1, padx=2, pady=2)

        button_15 = tk.Button(
            keypad,
            text="3",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("3")
        )
        button_15.grid(row=4, column=2, padx=2, pady=2)

        button_16 = tk.Button(
            keypad,
            text="-",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("-")
        )
        button_16.grid(row=4, column=3, padx=2, pady=2)

        button_17 = tk.Button(
            keypad,
            text="0",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("0")
        )
        button_17.grid(row=5, column=0, padx=2, pady=2)

        button_18 = tk.Button(
            keypad,
            text=".",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval(".")
        )
        button_18.grid(row=5, column=1, padx=2, pady=2)

        button_19 = tk.Button(
            keypad,
            text="=",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.result()
        )
        button_19.grid(row=5, column=2, padx=2, pady=2)

        button_20 = tk.Button(
            keypad,
            text="+",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("+")
        )
        button_20.grid(row=5, column=3, padx=2, pady=2)

    def addval(self, v):
        self.rovnice += v
        self.val.set(self.rovnice)

    def clear_num(self):
        self.rovnice = ""
        self.val.set("0")

    def remove_num(self):
        self.rovnice = self.rovnice[:-1]
        self.val.set(self.rovnice)

        if len(self.rovnice) == 0:
            self.rovnice = ""
            self.val.set("0")

        print(self.rovnice)

    def result(self):
        try:
            res = eval(self.rovnice)
            if res % 1 == 0:
                res = int(res)
            print(res)
            res = round(res, 5)
            self.val.set(str(res))
            self.rovnice = str(res)

        except SyntaxError:
            self.val.set("Error")
            self.rovnice = ""


root = Calculator()

# font.nametofont("TkDefaultFont").configure(size=15)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

root.mainloop()
