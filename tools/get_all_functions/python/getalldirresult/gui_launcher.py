import os
import tkinter, tkinter.filedialog
from tkinter import *
from tkinter import ttk
from subprocess import check_output

# --------------------------------------------------------------------------
# --- function definition

def call_mode1():
	check_output("python getalldirresult.py --mode 1", shell=True)

def call_mode2():
	check_output("python getalldirresult.py --mode 2", shell=True)

def call_depth_2():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items2 = []
	for line in f:
		items2.append(line)
	f.close()

	if len(items2) == 0:
		print("no more result")

	else:
		# -  
		def call_check_target(xxx):
			targe_module_name = items2[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		frame = ttk.Frame(root, padding=8)
		cb_val2 = StringVar()
		cb_val2.set('Select target module ( depth 1 )')
		cb2 = ttk.Combobox(frame, textvariable=cb_val2, height=15, width=50)
		cb2['values'] = items2
		frame.grid()
		cb2.grid()
		cb2.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb2.current())), call_mode1(), call_mode2(), call_depth_3()])

def call_depth_3():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items3 = []
	for line in f:
		items3.append(line)
	f.close()

	if len(items3) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items3[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val3 = StringVar()
		cb_val3.set('Select target module ( depth 2 )')
		cb3 = ttk.Combobox(frame, textvariable=cb_val3, height=15, width=50)
		cb3['values'] = items3
		frame.grid()
		cb3.grid()
		cb3.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb3.current())), call_mode1(), call_mode2(), call_depth_4()])


def call_depth_4():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items4 = []
	for line in f:
		items4.append(line)
	f.close()

	if len(items4) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items4[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val4 = StringVar()
		cb_val4.set('Select target module ( depth 3 )')
		cb4 = ttk.Combobox(frame, textvariable=cb_val4, height=15, width=50)
		cb4['values'] = items4
		frame.grid()
		cb4.grid()
		cb4.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb4.current())), call_mode1(), call_mode2(), call_depth_5()])


def call_depth_5():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items5 = []
	for line in f:
		items5.append(line)
	f.close()

	if len(items5) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items5[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val5 = StringVar()
		cb_val5.set('Select target module ( depth 4 )')
		cb5 = ttk.Combobox(frame, textvariable=cb_val5, height=15, width=50)
		cb5['values'] = items5
		frame.grid()
		cb5.grid()
		cb5.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb5.current())), call_mode1(), call_mode2(), call_depth_6()])


def call_depth_6():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items6 = []
	for line in f:
		items6.append(line)
	f.close()

	if len(items6) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items6[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val6 = StringVar()
		cb_val6.set('Select target module ( depth 5 )')
		cb6 = ttk.Combobox(frame, textvariable=cb_val6, height=15, width=50)
		cb6['values'] = items6
		frame.grid()
		cb6.grid()
		cb6.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb6.current())), call_mode1(), call_mode2(), call_depth_7()])



def call_depth_7():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items7 = []
	for line in f:
		items7.append(line)
	f.close()

	if len(items7) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items7[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val7 = StringVar()
		cb_val7.set('Select target module ( depth 6 )')
		cb7 = ttk.Combobox(frame, textvariable=cb_val7, height=15, width=50)
		cb7['values'] = items7
		frame.grid()
		cb7.grid()
		cb7.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb7.current())), call_mode1(), call_mode2(), call_depth_8()])


def call_depth_8():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items8 = []
	for line in f:
		items8.append(line)
	f.close()

	if len(items8) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items8[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val8 = StringVar()
		cb_val8.set('Select target module ( depth 7 )')
		cb8 = ttk.Combobox(frame, textvariable=cb_val8, height=15, width=50)
		cb8['values'] = items8
		frame.grid()
		cb8.grid()
		cb8.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb8.current())), call_mode1(), call_mode2(), call_depth_9()])


def call_depth_9():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items9 = []
	for line in f:
		items9.append(line)
	f.close()

	if len(items9) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items9[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val9 = StringVar()
		cb_val9.set ('Select target module ( depth 8 )')
		cb9 = ttk.Combobox(frame, textvariable=cb_val9, height=15, width=50)
		cb9['values'] = items9
		frame.grid()
		cb9.grid()
		cb9.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb9.current())), call_mode1(), call_mode2(), call_depth_10()])


def call_depth_10():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items10 = []
	for line in f:
		items10.append(line)
	f.close()

	if len(items10) == 0:
		print("no more result")
	else:
		# -
		def call_check_target(xxx):
			targe_module_name = items10[xxx]

			if '==' in targe_module_name:
				sep = '=='
				targe_module_name = targe_module_name.split(sep)[:-1]
				targe_module_name = targe_module_name[0]
			else:
				targe_module_name = targe_module_name.replace("\n", "")

			i = open("tmp/tmp.txt", mode="w")
			i.write(targe_module_name)
			i.close()
			check_output("python check_target.py", shell=True)

		# - 
		frame = ttk.Frame(root, padding=8)
		cb_val10 = StringVar()
		cb_val10.set('Select target module ( depth 9 )')
		cb10 = ttk.Combobox(frame, textvariable=cb_val10, height=15, width=50)
		cb10['values'] = items10
		frame.grid()
		cb10.grid()
		cb10.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb10.current())), call_mode1(), call_mode2()])

# --------------------------------------------------------------------------
# --- generate item lsit

# --- item lsit 1

# - get pip list
check_output("pip freeze > result/freeze_result.txt", shell=True)
f = open("result/freeze_result.txt", "r")
items = []
items.append("="*40)
items.append("="*15 + "  pip list  " +"="*15)
items.append("="*40)
for line in f:
	items.append(line)
f.close()

# - get buitin lib list
def get_buitin_lib_list(target_buitin_lib_path_list):
	
	# root = tkinter.Tk()
	# root.withdraw()
	# target_buitin_lib_path = tkinter.filedialog.askdirectory(parent=root,initialdir="/Users/jack/miniconda2/envs/",title='Please select a directory')
	listdir_result_object = os.listdir(target_buitin_lib_path)

	listdir_result_list = []
	for listdir_result in listdir_result_object:
		if "DS_Store" in listdir_result:
			pass
			# print(".DS_Store skipped")

		elif ".txt" in listdir_result:
			pass
			# print("*.txt skipped")

		else:
			# print(listdir_result)
			listdir_result = listdir_result.replace(".py", "")
			listdir_result_list.append(listdir_result)

	listdir_result_list.sort()

	items.append("="*40)
	items.append(target_buitin_lib_path)
	items.append("="*40)
	for builtin_lib_package_n_module in listdir_result_list:
		items.append(builtin_lib_package_n_module)
		# print(builtin_lib_package_n_module)


target_buitin_lib_path_list = [
								"/Users/jack/miniconda2/envs/py27/lib/python2.7/", 
								"/Users/jack/miniconda2/envs/py36/lib/python3.6/", 
								"/Users/jack/miniconda2/envs/py37/lib/python3.6/"
							]

for target_buitin_lib_path in target_buitin_lib_path_list:
	get_buitin_lib_list(target_buitin_lib_path_list)

# - debugging
# print("="*50 + "debugging" + "="*50)
# print("items type: ", type(items))
# print("items : ", items)
# print("="*50 + "debugging" + "="*50)


# --------------------------------------------------------------------------
# --- Tk window

# -  
def call_check_target(xxx):
	targe_module_name = items[xxx]

	if '==' in targe_module_name:
		sep = '=='
		targe_module_name = targe_module_name.split(sep)[:-1]
		targe_module_name = targe_module_name[0]
	else:
		targe_module_name = targe_module_name.replace("\n", "")

	i = open("tmp/tmp.txt", mode="w")
	i.write(targe_module_name)
	i.close()
	check_output("python check_target.py", shell=True)

# -  
root = Tk()
root.title("Python Library Help Viewer")
frame = ttk.Frame(root, padding=8)

#
def new_widget():
    check_output("python gui_launcher.py", shell=True)




def new_widget2():  
	root2 = Tk()
	root2.title("Python Library Help Viewer")
	frame = ttk.Frame(root2, padding=8)

	#
	def new_widget():
	    check_output("python gui_launcher.py", shell=True)

	def edit_namepace_checker():
	    check_output("open module_namespace_checker.py", shell=True)

	def open_help_text_folder():
	    check_output("open result/help_docs/", shell=True)

	def close():
	    quit()

	b1 = Button(frame, text="New Wideget", command=lambda:[root2.iconify(), new_widget2()])
	b2 = Button(frame, text="Namespace Checker", command=edit_namepace_checker)
	b3 = Button(frame, text="Help Docs Folder", command=open_help_text_folder)
	# b4 = Button(frame, text="Close Wideget", command=quit)
	b4 = Button(frame, text="Close Wideget", command=lambda:[quit()])
	b1.grid(row=0, sticky=E)
	b2.grid(row=0, sticky=W)
	b3.grid(row=1, sticky=W)
	b4.grid(row=1, sticky=E)

	#
	cb_val = StringVar()
	cb_val.set('Select target module')
	cb = ttk.Combobox(frame, textvariable=cb_val, height=15, width=50)
	cb['values'] = items
	frame.grid()
	cb.grid()
	cb.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb.current())), call_mode1(), call_mode2(), call_depth_2()])
	root2.mainloop()






def edit_namepace_checker():
    check_output("open module_namespace_checker.py", shell=True)

def open_help_text_folder():
    check_output("open result/help_docs/", shell=True)

def close():
    quit()

# b1 = Button(frame, text="New Wideget", command=lambda:[root.iconify(), new_widget()])
b1 = Button(frame, text="New Wideget", command=lambda:[root.iconify(), new_widget2()])
b2 = Button(frame, text="Namespace Checker", command=edit_namepace_checker)
b3 = Button(frame, text="Help Docs Folder", command=open_help_text_folder)
# b4 = Button(frame, text="Close Wideget", command=quit)
b4 = Button(frame, text="Close Wideget", command=lambda:[quit()])
b1.grid(row=0, sticky=E)
b2.grid(row=0, sticky=W)
b3.grid(row=1, sticky=W)
b4.grid(row=1, sticky=E)

#
cb_val = StringVar()
cb_val.set('Select target module')
cb = ttk.Combobox(frame, textvariable=cb_val, height=15, width=50)
cb['values'] = items
frame.grid()
cb.grid()
cb.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb.current())), call_mode1(), call_mode2(), call_depth_2()])
root.mainloop()

