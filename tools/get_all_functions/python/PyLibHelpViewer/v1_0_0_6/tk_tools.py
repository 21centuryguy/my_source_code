"""
http://effbot.org/zone/tkinter-scrollbar-patterns.htm

"""
#---------------------------------------------
from tkinter import *
from subprocess import check_output

#---------------------------------------------
def show_result_text_list():
	root = Tk()
	root.title("Help text from soure code")

	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT, fill=Y)

	listbox = Listbox(root)
	listbox.pack()

	f = open("result/result.txt", "r")
	f = f.read().splitlines()
	for line in f:
		# line = line.replace("=", "")
		# line = line.replace(" ", "")
		if len(line) > 0:
			listbox.insert(END, line)
		else:
			pass

	listbox.config(yscrollcommand=scrollbar.set, bd=1, height=63, width=100)
	scrollbar.config(command=listbox.yview)

	Button(root, text='Close', command=quit).pack()

	root.mainloop()

#---------------------------------------------
def show_verified_package_class_list():
	root = Tk()
	root.title("Available Package and Single file List")

	scrollbar = Scrollbar(root)
	scrollbar.pack(side=RIGHT, fill=Y)

	listbox = Listbox(root)
	listbox.pack()

	f = open("result/verified_package_class_list.txt", "r")
	f = f.read().splitlines()
	for line in f:
		# line = line.replace("=", "")
		line = line.replace(" ", "")
		if len(line) > 0:
			listbox.insert(END, line)
		else:
			pass

	listbox.config(yscrollcommand=scrollbar.set, bd=1, height=63, width=40)
	scrollbar.config(command=listbox.yview)

	Button(root, text='Close', command=quit).pack()

	root.mainloop()

#---------------------------------------------
def tk_tools_main(option):
	if option == 1:
		show_result_text_list()
	if option == 2:
		show_verified_package_class_list()

if __name__ == "__main__":
	tk_tools_main(option)

