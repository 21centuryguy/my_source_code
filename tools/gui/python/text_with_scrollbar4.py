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

listbox.config(yscrollcommand=scrollbar.set, bd=1, height=30, width=40)
scrollbar.config(command=listbox.yview)

mainloop()
