import tkinter as tk
from tkinter import ttk


root = tk.Tk()

def tiskni(event):
    print("ahoj")
    print(event)

root.geometry("200x200+600+600")



root.bind("<a>", tiskni)






root.mainloop()