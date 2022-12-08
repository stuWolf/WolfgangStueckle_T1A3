import tkinter as tk
from tkinter import ttk

class App():

    def __init__(self):
        self.root = tk.Tk()

        ttk.Label(self.root, text = 'label text', justify = 'center').grid(row=0, column=0)
        self.string = [tk.StringVar()]
        self.string[0].set('entry text')
        ttk.Entry(self.root, textvariable = self.string[0]).grid(row=0, column=1)
        self.mainButton = ttk.Button(self.root, text = 'BUTTON', command=self.callback)
        self.mainButton.grid(row = 1, columnspan = 2)

        self.root.mainloop()

    def callback(self):
        self.mainButton.grid_forget()
        self.string.append(tk.StringVar())
        l = len(self.string)
        self.string[l-1].set('entry text')
        ttk.Label(self.root, text = 'label text', justify = 'center').grid(row=l-1, column=0)
        ttk.Entry(self.root, textvariable = self.string[l-1]).grid(row=l-1, column=1)
        self.mainButton.grid(row = l, columnspan = 2)

App()