import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.png")

# w1 = tk.Label(root, image=logo).pack(side="right")
w1 = tk.Label(root, image=logo).pack(side="top")

explanation = ""
f = open("sample_list.txt", "r")
for line in f:
	print(type(line))
	# print(line)

	explanation = explanation + line

# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface 
# exists to allow additional image file
# formats to be added easily."""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")

root.mainloop()
