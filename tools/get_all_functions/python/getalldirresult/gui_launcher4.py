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

	# - 
	root2 = Tk()
	root2.title("Python Library Help Viewer 2")
	frame2 = ttk.Frame(root2, padding=8)
	cb_val2 = StringVar()
	cb_val2.set('Select target module 2')
	cb2 = ttk.Combobox(frame2, textvariable=cb_val2, height=15, width=50)
	cb2['values'] = items2
	frame2.grid()
	cb2.grid()
	cb2.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb2.current())), call_mode1(), call_mode2(), call_depth_3()])
	def call_back(): quit();
	b = Button(frame2, text="Quit", command=call_back); b.grid()
	root2.mainloop()

def call_depth_3():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items3 = []
	for line in f:
		items3.append(line)
	f.close()

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
	root3 = Tk()
	root3.title("Python Library Help Viewer 3")
	frame3 = ttk.Frame(root3, padding=8)
	cb_val3 = StringVar()
	cb_val3.set('Select target module 3')
	cb3 = ttk.Combobox(frame3, textvariable=cb_val3, height=15, width=50)
	cb3['values'] = items3
	frame3.grid()
	cb3.grid()
	cb3.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb3.current())), call_mode1(), call_mode2(), call_depth_4()])
	root3.mainloop()


def call_depth_4():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items4 = []
	for line in f:
		items4.append(line)
	f.close()

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
	root4 = Tk()
	root4.title("Python Library Help Viewer 4")
	frame4 = ttk.Frame(root4, padding=8)
	cb_val4 = StringVar()
	cb_val4.set('Select target module 4')
	cb4 = ttk.Combobox(frame4, textvariable=cb_val4, height=15, width=50)
	cb4['values'] = items4
	frame4.grid()
	cb4.grid()
	cb4.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb4.current())), call_mode1(), call_mode2(), call_depth_5()])
	root4.mainloop()


def call_depth_5():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items5 = []
	for line in f:
		items5.append(line)
	f.close()

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
	root5 = Tk()
	root5.title("Python Library Help Viewer 5")
	frame5 = ttk.Frame(root5, padding=8)
	cb_val5 = StringVar()
	cb_val5.set('Select target module 5')
	cb5 = ttk.Combobox(frame5, textvariable=cb_val5, height=15, width=50)
	cb5['values'] = items5
	frame5.grid()
	cb5.grid()
	cb5.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb5.current())), call_mode1(), call_mode2(), call_depth_6()])
	root5.mainloop()


def call_depth_6():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items6 = []
	for line in f:
		items6.append(line)
	f.close()

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
	root6 = Tk()
	root6.title("Python Library Help Viewer 6")
	frame6 = ttk.Frame(root6, padding=8)
	cb_val6 = StringVar()
	cb_val6.set('Select target module 6')
	cb6 = ttk.Combobox(frame6, textvariable=cb_val6, height=15, width=50)
	cb6['values'] = items6
	frame6.grid()
	cb6.grid()
	cb6.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb6.current())), call_mode1(), call_mode2(), call_depth_7()])
	root6.mainloop()



def call_depth_7():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items7 = []
	for line in f:
		items7.append(line)
	f.close()

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
	root7 = Tk()
	root7.title("Python Library Help Viewer 7")
	frame7 = ttk.Frame(root7, padding=8)
	cb_val7 = StringVar()
	cb_val7.set('Select target module 7')
	cb7 = ttk.Combobox(frame7, textvariable=cb_val7, height=15, width=50)
	cb7['values'] = items7
	frame7.grid()
	cb7.grid()
	cb7.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb7.current())), call_mode1(), call_mode2(), call_depth_8()])
	root7.mainloop()


def call_depth_8():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items8 = []
	for line in f:
		items8.append(line)
	f.close()

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
	root8 = Tk()
	root8.title("Python Library Help Viewer 8")
	frame8 = ttk.Frame(root8, padding=8)
	cb_val8 = StringVar()
	cb_val8.set('Select target module 8')
	cb8 = ttk.Combobox(frame8, textvariable=cb_val8, height=15, width=50)
	cb8['values'] = items8
	frame8.grid()
	cb8.grid()
	cb8.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb8.current())), call_mode1(), call_mode2(), call_depth_9()])
	root8.mainloop()


def call_depth_9():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items9 = []
	for line in f:
		items9.append(line)
	f.close()

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
	root9 = Tk()
	root9.title("Python Library Help Viewer 9")
	frame9 = ttk.Frame(root9, padding=8)
	cb_val9 = StringVar()
	cb_val9.set('Select target module 9')
	cb9 = ttk.Combobox(frame9, textvariable=cb_val9, height=15, width=50)
	cb9['values'] = items9
	frame9.grid()
	cb9.grid()
	cb9.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb9.current())), call_mode1(), call_mode2(), call_depth_10()])
	root9.mainloop()


def call_depth_10():
	# - get item lsit 
	f = open("result/verified_package_class_list.txt", "r")
	items10 = []
	for line in f:
		items10.append(line)
	f.close()

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
	root10 = Tk()
	root10.title("Python Library Help Viewer 10")
	frame10 = ttk.Frame(root10, padding=8)
	cb_val10 = StringVar()
	cb_val10.set('Select target module 10')
	cb10 = ttk.Combobox(frame10, textvariable=cb_val10, height=15, width=50)
	cb10['values'] = items10
	frame10.grid()
	cb10.grid()
	cb10.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb10.current())), call_mode1(), call_mode2()])
	root10.mainloop()

# --------------------------------------------------------------------------
# --- generate item lsit

# - item lsit 1
check_output("pip freeze > result/freeze_result.txt", shell=True)
f = open("result/freeze_result.txt", "r")
items = []
for line in f:
	items.append(line)
f.close()
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
root.title("Python Library Help Viewer 1")
frame = ttk.Frame(root, padding=8)
cb_val = StringVar()
cb_val.set('Select target module')
cb = ttk.Combobox(frame, textvariable=cb_val, height=15, width=50)
cb['values'] = items
frame.grid()
cb.grid()
cb.bind('<<ComboboxSelected>>', lambda e:[call_check_target(int(cb.current())), call_mode1(), call_mode2(), call_depth_2()])
def call_back(): quit();
b = Button(frame, text="Quit", command=call_back); b.grid()
root.mainloop()


