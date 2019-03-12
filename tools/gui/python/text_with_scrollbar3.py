"""
http://effbot.org/zone/tkinter-scrollbar-patterns.htm

"""

from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root)
listbox.pack()


f = open("sample_list.txt", "r")
f = f.read().splitlines()
for line in f:
	line = line.replace("=", "")
	line = line.replace(" ", "")
	if len(line) > 0:
		listbox.insert(END, line)
	else:
		pass

"""
for i in range(100):
    listbox.insert(END, i)
"""


# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

mainloop()


"""
from Tkinter import *

master = Tk()

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

mainloop()
"""

"""
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

myscroll = ttk.Scrollbar(myframe, orient='horizontal', command=myentry.xview)
myentry.config(xscrollcommand=myscroll.set)

myframe.grid()
myentry.grid(row=1, sticky='ew')
myscroll.grid(row=2, sticky='ew')

root.mainloop()
"""