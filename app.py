import tkinter as tk
from tkinter import ttk
# import tkinter.font as font


RED = "red"
BLACK = "black"


class Calculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kabub Calculator")

        self.geometry("350x470+1000+800")
        # self.resizable(False, False)

        self.val = tk.StringVar()
        self.val.set("0")
        self.rovnice = ""

        self.container = ttk.Frame(self, relief="ridge")
        self.container.grid(row=0, column=0, padx=(10, 10), sticky="nsew")

        self.display = ttk.Label(self.container, font=("Segoe UI bold", 30), textvariable=self.val)
        self.display.grid(row=0, column=0, sticky="ne", padx=15, pady=20)

        self.keypad = ttk.Frame(self.container)
        self.keypad.grid(row=1, column=0, sticky="swe", padx=10, pady=10)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # Keypad buttons
        self.button_01 = tk.Button(
            self.keypad,
            text="C",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.clear_num()

        )
        self.button_01.grid(row=1, column=0, padx=2, pady=2)
        self.bind("<c>", lambda x: self.clear_num())

        # button_02 = tk.Button(
        #     keypad,
        #     text="NA",
        #     height=1,
        #     width=4,
        #     font=("Segoe UI bold", 20),
        #     cursor="hand2",
        #     foreground=BLACK,
        #     # command=lambda: self.addval("")
        #
        # )
        # button_02.grid(row=1, column=1, padx=2, pady=2)
        #
        # button_03 = tk.Button(
        #     keypad,
        #     text="NA",
        #     height=1,
        #     width=4,
        #     font=("Segoe UI bold", 20),
        #     foreground=BLACK,
        #     # command=lambda: self.addval("")
        # )
        # button_03.grid(row=1, column=2, padx=2, pady=2)
        self.kp = ttk.Style()

        self.button_04 = ttk.Button(
            self.keypad,
            text="DEL",
            cursor="hand2",
            command=lambda: self.remove_num()
        )
        self.button_04.grid(row=1, column=3, padx=2, pady=2, ipady=40)
        self.kp.configure("TButton", background="blue", font=("Helvetica bold", 20))
        self.bind("<BackSpace>", lambda x: self.remove_num())

        self.button_05 = tk.Button(
            self.keypad,
            text="7",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("7")
        )
        self.button_05.grid(row=2, column=0, padx=2, pady=2)
        self.bind("<Key-7>", lambda x: self.addval("7"))

        self.button_06 = tk.Button(
            self.keypad,
            text="8",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("8")
        )
        self.button_06.grid(row=2, column=1, padx=2, pady=2)
        self.bind("<8>", lambda x: self.addval("8"))

        self.button_07 = tk.Button(
            self.keypad,
            text="9",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("9")
        )
        self.button_07.grid(row=2, column=2, padx=2, pady=2)
        self.bind("<Key-9>", lambda x: self.addval("9"))

        self.button_08 = tk.Button(
            self.keypad,
            text="/",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("/")
        )
        self.button_08.grid(row=2, column=3, padx=2, pady=2)
        self.bind("<slash>", lambda x: self.addval("/"))

        self.button_09 = tk.Button(
            self.keypad,
            text="4",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("4")
        )
        self.button_09.grid(row=3, column=0, padx=2, pady=2)
        self.bind_all("<Key-4>", lambda x: self.addval("4"))

        self.button_10 = tk.Button(
            self.keypad,
            text="5",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("5")
        )
        self.button_10.grid(row=3, column=1, padx=2, pady=2)
        self.bind("<Key-5>", lambda x: self.addval("5"))

        self.button_11 = tk.Button(
            self.keypad,
            text="6",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("6")
        )
        self.button_11.grid(row=3, column=2, padx=2, pady=2)
        self.bind("<Key-6>", lambda x: self.addval("6"))

        self.button_12 = tk.Button(
            self.keypad,
            text="*",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("*")
        )
        self.button_12.grid(row=3, column=3, padx=2, pady=2)
        self.bind("<asterisk>", lambda x: self.addval("*"))

        self.button_13 = tk.Button(
            self.keypad,
            text="1",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("1")
        )
        self.button_13.grid(row=4, column=0, padx=2, pady=2)
        self.bind("<Key-1>", lambda x: self.addval("1"))

        self.button_14 = tk.Button(
            self.keypad,
            text="2",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("2")
        )
        self.button_14.grid(row=4, column=1, padx=2, pady=2)
        self.bind("<Key-2>", lambda x: self.addval("2"))

        self.button_15 = tk.Button(
            self.keypad,
            text="3",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("3")
        )
        self.button_15.grid(row=4, column=2, padx=2, pady=2)
        self.bind("<Key-3>", lambda x: self.addval("3"))

        self.button_16 = tk.Button(
            self.keypad,
            text="-",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("-")
        )
        self.button_16.grid(row=4, column=3, padx=2, pady=2)
        self.bind("<minus>", lambda x: self.addval("-"))

        self.button_17 = tk.Button(
            self.keypad,
            text="0",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("0")
        )
        self.button_17.grid(row=5, column=0, padx=2, pady=2)
        self.bind("<Key-0>", lambda x: self.addval("0"))

        self.button_18 = tk.Button(
            self.keypad,
            text=".",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval(".")
        )
        self.button_18.grid(row=5, column=1, padx=2, pady=2)
        self.bind("<.>", lambda x: self.addval("."))

        self.button_19 = tk.Button(
            self.keypad,
            text="=",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.result()
        )
        self.button_19.grid(row=5, column=2, padx=2, pady=2)
        self.bind("<Return>", lambda x: self.result())

        self.button_20 = tk.Button(
            self.keypad,
            text="+",
            height=1,
            width=4,
            font=("Segoe UI bold", 20),
            foreground=BLACK,
            command=lambda: self.addval("+")
        )
        self.button_20.grid(row=5, column=3, padx=2, pady=2)
        self.bind("<plus>", lambda x: self.addval("+"))

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
