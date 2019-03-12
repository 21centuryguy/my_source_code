import tkinter as tk

def single_root():
	root = tk.Tk()
	logo = tk.PhotoImage(file="python_logo_small.gif")

	w1 = tk.Label(root, image=logo).pack(side="right")

	explanation = """At present, only GIF and PPM/PGM
	formats are supported, but an interface 
	exists to allow additional image file
	formats to be added easily."""

	w2 = tk.Label(root, 
	              justify=tk.LEFT,
	              padx = 10, 
	              text=explanation).pack(side="left")
	root.mainloop()


def double_root():
	root = tk.Tk()
	root2 = tk.Tk()

	logo = tk.PhotoImage(file="python_logo_small.gif")

	w1 = tk.Label(root, image=logo).pack(side="right")

	explanation = """At present, only GIF and PPM/PGM
	formats are supported, but an interface 
	exists to allow additional image file
	formats to be added easily."""

	w2 = tk.Label(root2, 
	              justify=tk.LEFT,
	              padx = 10, 
	              text=explanation).pack(side="left")

	root.mainloop()
	root2.mainloop()


single_root()
double_root()
