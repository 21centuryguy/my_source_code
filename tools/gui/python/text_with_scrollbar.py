import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# mytext = tk.StringVar(value='test ' * 30)
explanation = ""
f = open("sample_list.txt", "r")
for line in f:
	explanation = explanation + line
mytext = tk.StringVar(value = explanation)

myframe = ttk.Frame(root)
myentry = ttk.Entry(myframe, textvariable=mytext, state='readonly')

# myscroll = ttk.Scrollbar(myframe, orient='horizontal', command=myentry.xview)
myscroll = ttk.Scrollbar(myframe, command=myentry.xview)

myentry.config(xscrollcommand=myscroll.set)

myframe.grid()
myentry.grid(row=1, sticky='ew')
myscroll.grid(row=2, sticky='ew')

root.mainloop()
