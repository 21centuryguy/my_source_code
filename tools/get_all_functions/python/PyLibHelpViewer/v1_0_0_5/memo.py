from subprocess import check_output

#---------------------------------------------
def call_mode1():
	check_output("python getalldirresult.py --mode 2", shell=True)

def call_mode2():
	check_output("python getalldirresult.py --mode 2", shell=True)


#---------------------------------------------
Button(root, text='close', command=lambda:[call_mode2(), quit()]).pack()

root.mainloop()
# root.iconify()