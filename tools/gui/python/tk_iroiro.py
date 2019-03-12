# ---------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import ttk

# ---------------------------------------
def import_styel_1():
	root = tk.Tk()
	w = tk.Label(root, text="Hello Tkinter! (style 1)")
	w.pack()
	root.mainloop()

# ---------------------------------------
def import_styel_2():
	root = Tk()
	ttk.Button(root, text="Hello World (style 2)").grid()
	root.mainloop()

# ---------------------------------------
def window_title():
	root = Tk()
	root.title("Feet to Meters")
	root.mainloop()

# ---------------------------------------
def main(mode):

	if mode == 1:
		import_styel_1()

	if mode == 2:
		import_styel_2()

	if mode == 3:
		window_title()

# ---------------------------------------
if __name__ == "__main__":
	import optparse
	parser = optparse.OptionParser()

	parser.add_option('-q', '--mode',
		action="store", dest="mode",
		help="mode1: get help text of tareget, mode2: get package list from target, mode3: generate target import line", default="spam")
	options, args = parser.parse_args()
	mode = int(options.mode)

	main(mode)

