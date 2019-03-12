"""
https://www.python-course.eu/tkinter_labels.php
"""

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.png")

w1 = tk.Label(root, image=logo).pack(side="top")

explanation = ""
f = open("sample_list.txt", "r")
for line in f:
	explanation = explanation + line

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")

root.mainloop()
