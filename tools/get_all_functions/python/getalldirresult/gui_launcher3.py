from tkinter import *
from tkinter import ttk
from subprocess import check_output


# --------------------------------------------------------------------------
# --- function definition

def call_check_target():
	targe_module_name = items[int(cb.current())]
	sep = '=='
	targe_module_name = targe_module_name.split(sep)[:-1]
	targe_module_name = targe_module_name[0]
	i = open("tmp/tmp.txt", mode="w")
	i.write(targe_module_name)
	i.close()
	check_output("python check_target.py", shell=True)

def call_mode1():
	check_output("python getalldirresult.py --mode 1", shell=True)

def call_mode2():
	check_output("python getalldirresult.py --mode 2", shell=True)

def call_check_target2():
	targe_module_name = items2[int(cb.current())]
	sep = '=='
	targe_module_name = targe_module_name.split(sep)[:-1]
	targe_module_name = targe_module_name[0]
	i = open("tmp/tmp.txt", mode="w")
	i.write(targe_module_name)
	i.close()
	check_output("python check_target.py", shell=True)



# --------------------------------------------------------------------------
# --- get list

# ------------------------
# --- generate item 1 lsit
check_output("pip freeze > result/freeze_result.txt", shell=True)
f = open("result/freeze_result.txt", "r")
items = []
for line in f:
	items.append(line)
# - debugging
print("="*50 + "debugging" + "="*50)
print("items type: ", type(items))
print("items : ", items)
print("="*50 + "debugging" + "="*50)

# ------------------------
# --- generate item 2 lsit
f2 = open("result/verified_package_class_list.txt", "r")
items2 = []
for line in f2:
	items2.append(line)
# - debugging
print("="*50 + "debugging" + "="*50)
print("items type: ", type(items2))
print("items : ", items)
print("="*50 + "debugging" + "="*50)


# --------------------------------------------------------------------------
# --- tk

# ------------------------
# --- Tk window
root = Tk()
root.title("Python Library Help Viewer")

# ------------------------
# --- 1st dropdown menu
frame = ttk.Frame(root, padding=8)

cb_val = StringVar()
cb_val.set('Select target module')
cb = ttk.Combobox(frame, textvariable=cb_val, height=15, width=50)
cb['values'] = items

statusmsg = StringVar()

frame.grid()
cb.grid()
print("="*50)
cb.bind('<<ComboboxSelected>>', lambda e:[call_check_target(), call_mode1(), call_mode2()])

# ------------------------
# --- 2nd dropdown menu
frame2 = ttk.Frame(root, padding=8)

cb_val2 = StringVar()
cb_val2.set('Select target package and class')
cb2 = ttk.Combobox(frame2, textvariable=cb_val2, height=15, width=50)
cb2['values'] = items2

frame2.grid()
cb2.grid()
cb2.bind('<<ComboboxSelected>>', lambda e:[call_mode2()])

# ------------------------
# --- Tk window
root.mainloop()

