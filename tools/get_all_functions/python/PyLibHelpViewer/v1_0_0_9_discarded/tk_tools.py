# -*- Coding: utf-8 -*-

"""
http://effbot.org/zone/tkinter-scrollbar-patterns.htm

"""
#---------------------------------------------
from tkinter import *
from subprocess import check_output

#---------------------------------------------
def open_module_path():
	result_txt_line_list = []
	i = open("result/result.txt", "r")
	for result_txt_line in i:
		result_txt_line_list.append(result_txt_line)
	last_checked_module_file_path = result_txt_line_list[-3]
	target_slicing_position = last_checked_module_file_path.rfind("/")
	last_checked_module_path = last_checked_module_file_path[0:target_slicing_position]
	commnad_line = "open " + last_checked_module_path
	check_output(commnad_line , shell=True)

def open_module_file():
	result_txt_line_list = []
	i = open("result/result.txt", "r")
	for result_txt_line in i:
		result_txt_line_list.append(result_txt_line)
	last_checked_module_file_path = result_txt_line_list[-3]
	commnad_line = "open " + last_checked_module_file_path
	check_output(commnad_line , shell=True)

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

	listbox.config(yscrollcommand=scrollbar.set, bd=1, height=33, width=100)
	scrollbar.config(command=listbox.yview)

	Button(root, text='Close', command=quit).pack(side="left", padx="60", pady="5")
	Button(root, text='Open File', command=open_module_file).pack(side="right", padx="60", pady="5")
	Button(root, text='Open Folder', command=open_module_path).pack(side="right", padx="200", pady="5")


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

	listbox.config(yscrollcommand=scrollbar.set, bd=1, height=33, width=40)
	scrollbar.config(command=listbox.yview)

	Button(root, text='Close', command=quit).pack()

	root.mainloop()

#---------------------------------------------
def tk_tools_main(option):
	if option == 1:
		show_result_text_list()
	if option == 2:
		# show_verified_package_class_list()
		pass

if __name__ == "__main__":
	tk_tools_main(option)

