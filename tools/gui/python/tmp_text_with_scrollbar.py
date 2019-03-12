"""
https://stackoverflow.com/questions/13832720/how-to-attach-a-scrollbar-to-a-text-widget
"""

import tkinter as tki # Tkinter -> tkinter in Python3
from tkinter import ttk

class App(object):

    def __init__(self):
        self.root = tki.Tk()

    # create a Frame for the Text and Scrollbar
        txt_frm = tki.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        explanation = ""
        f = open("sample_list.txt", "r")
        for line in f:
            explanation = explanation + line
        mytext = tki.StringVar(value = explanation)
        txt = ttk.Entry(txt_frm, textvariable=mytext)

    # create a Text widget
        self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.config(font=("consolas", 10))
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

app = App()
app.root.mainloop()
