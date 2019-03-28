from tkinter import *
from tkinter import ttk
from subprocess import check_output
import pyperclip

# ---------------------------------------
# ---------------------------------------
# --- generate item lsit

# - item lsit 1
f = open("copy_list1.txt", "r")
items = []
for line in f:
	items.append(line)
f.close()

# - item lsit 2
f = open("copy_list2.txt", "r")
items2 = []
for line in f:
	items2.append(line)
f.close()

# - item lsit 3
f = open("copy_list3.txt", "r")
items3 = []
for line in f:
	items3.append(line)
f.close()

# - item lsit 4
f = open("copy_list4.txt", "r")
items4 = []
for line in f:
	items4.append(line)
f.close()

# - item lsit 5
f = open("copy_list5.txt", "r")
items5 = []
for line in f:
	items5.append(line)
f.close()

# ---------------------------------------
# ---------------------------------------
# --- func definition

# - func 1
def edit_item_list1():
    check_output("open copy_list1.txt", shell=True)

# - func 2
def edit_item_list2():
    check_output("open copy_list2.txt", shell=True)

# - func 3
def edit_item_list3():
    check_output("open copy_list3.txt", shell=True)

# - func 4
def edit_item_list4():
    check_output("open copy_list4.txt", shell=True)

# - func 5
def edit_item_list5():
    check_output("open copy_list5.txt", shell=True)

# -------

# - func 6
def copy_selected_item(list, selected_item_num):
    selected_item = list[selected_item_num]
    pyperclip.copy(selected_item)
    print(selected_item)

# - func 7
def copy_selected_item_no_linebreak(list, selected_item_num):
    selected_item = list[selected_item_num]
    selected_item = selected_item.replace("\n", "")
    pyperclip.copy(selected_item)
    print(selected_item)

# ---------------------------------------
# ---------------------------------------
# --- root
# -
root = Tk()
root.title("CopyList")



# ---------------------------------------
# ---------------------------------------
# --- frame

# -- frame 1
frame = ttk.Frame(root, padding=8)

# -- frame 2
frame2 = ttk.Frame(root, padding=8)

# -- frame 3
frame3 = ttk.Frame(root, padding=8)

# -- frame 4
frame4 = ttk.Frame(root, padding=8)

# -- frame 5
frame5 = ttk.Frame(root, padding=8)



# ---------------------------------------
# ---------------------------------------
# --- combo box

# --- combo box 1
cb_val = StringVar()
cb_val.set("Copyitmes with linebreak")
cb = ttk.Combobox(frame, textvariable=cb_val, height=10, width=30)
cb['values'] = items
frame.grid()
cb.grid(row=2)
cb.bind('<<ComboboxSelected>>', lambda e:[copy_selected_item(items, int(cb.current()))])


# --- combo box 2
cb_val2 = StringVar()
cb_val2.set("Copyitmes without linebreak")
cb2 = ttk.Combobox(frame2, textvariable=cb_val2, height=10, width=30)
cb2['values'] = items2
frame2.grid()
cb2.grid(row=2)
cb2.bind('<<ComboboxSelected>>', lambda e:[copy_selected_item_no_linebreak(items2, int(cb2.current()))])


# --- combo box 3
cb_val3 = StringVar()
cb_val3.set("Copyitmes without linebreak")
cb3 = ttk.Combobox(frame3, textvariable=cb_val3, height=10, width=30)
cb3['values'] = items3
frame3.grid()
cb3.grid(row=2)
cb3.bind('<<ComboboxSelected>>', lambda e:[copy_selected_item_no_linebreak(items3, int(cb3.current()))])


# --- combo box 4
cb_val4 = StringVar()
cb_val4.set("Copyitmes without linebreak")
cb4 = ttk.Combobox(frame4, textvariable=cb_val4, height=10, width=30)
cb4['values'] = items4
frame4.grid()
cb4.grid(row=2)
cb4.bind('<<ComboboxSelected>>', lambda e:[copy_selected_item_no_linebreak(items4, int(cb4.current()))])


# --- combo box 5
cb_val5 = StringVar()
cb_val5.set("Copyitmes without linebreak")
cb5 = ttk.Combobox(frame5, textvariable=cb_val5, height=10, width=30)
cb5['values'] = items5
frame5.grid()
cb5.grid(row=2)
cb5.bind('<<ComboboxSelected>>', lambda e:[copy_selected_item_no_linebreak(items5, int(cb5.current()))])


# ---------------------------------------
# ---------------------------------------
# --- label

lb1 = Label(frame, text="Copylist 1", bg="mistyrose", font=("Helvetica 14" ))
lb2 = Label(frame2, text="Copylist 2", bg="mistyrose", font=("Helvetica 14"))
lb3 = Label(frame3, text="Copylist 3", bg="mistyrose", font=("Helvetica 14"))
lb4 = Label(frame4, text="Copylist 4", bg="mistyrose", font=("Helvetica 14"))
lb5 = Label(frame5, text="Copylist 5", bg="mistyrose", font=("Helvetica 14"))

frame.grid(); lb1.grid(row=0, sticky=W)
frame2.grid(); lb2.grid(row=0, sticky=W)
frame3.grid(); lb3.grid(row=0, sticky=W)
frame4.grid(); lb4.grid(row=0, sticky=W)
frame5.grid(); lb5.grid(row=0, sticky=W)


# ---------------------------------------
# ---------------------------------------
# --- button

b1 = Button(frame, text="Edit", command=lambda:[edit_item_list1()])
b2 = Button(frame2, text="Edit", command=lambda:[edit_item_list2()])
b3 = Button(frame3, text="Edit", command=lambda:[edit_item_list3()])
b4 = Button(frame4, text="Edit", command=lambda:[edit_item_list4()])
b5 = Button(frame5, text="Edit", command=lambda:[edit_item_list5()])

frame.grid(); b1.grid(row=0, sticky=E)
frame2.grid(); b2.grid(row=0, sticky=E)
frame3.grid(); b3.grid(row=0, sticky=E)
frame4.grid(); b4.grid(row=0, sticky=E)
frame5.grid(); b5.grid(row=0, sticky=E)



# ---------------------------------------
# ---------------------------------------
# --- call root
root.mainloop()
