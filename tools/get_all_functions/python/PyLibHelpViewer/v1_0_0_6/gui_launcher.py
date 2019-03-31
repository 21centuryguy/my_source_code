from tkinter import *
from tkinter import ttk
from subprocess import check_output

# ------------------------
# --- 
def call_mode1():
	check_output("python getalldirresult.py --mode 1", shell=True)

def call_mode2():
	check_output("python getalldirresult.py --mode 2", shell=True)

# ------------------------
# --- generate item lsit
items = ["Item %d" % (i+1,) for i in range(100)] # 전체 리스트 갯수
# - debugging
print("="*50 + "debugging" + "="*50)
print("items type: ", type(items))
print("items : ", items)
print("="*50 + "debugging" + "="*50)

# ------------------------
# --- generate [item, item description dict ]
d = dict(zip(items, [i + ' description.' for i in items]))
# - debugging
print("="*50 + "debugging" + "="*50)
print("d type: ", type(d))
print("d : ", d)
print("="*50 + "debugging" + "="*50)

# ------------------------
# ---
root = Tk()
root.title("Select target module name")
frame = ttk.Frame(root, padding=8)

cb_val = StringVar()
cb_val.set('Item 1')
cb = ttk.Combobox(frame, textvariable=cb_val, height=15) # 스크롤 없이 보이는 리스트 갯수
cb['values'] = sorted(d.keys())

frame.grid()
cb.grid()
cb.bind('<<ComboboxSelected>>', lambda e:[call_mode1(), call_mode2()])

root.mainloop()
