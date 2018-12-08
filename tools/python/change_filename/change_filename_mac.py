import re
import os
import tkinter, tkinter.filedialog

def change_filename():

	root = tkinter.Tk()
	root.withdraw()
	dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

	i = 1
	for fileName in os.listdir(dirname):
		# new_fileName = re.sub(r" ?\([^)]+\)", "", fileName)
		# new_fileName = re.sub(r"aaa", "bbb", fileName)
		# print(new_fileName)
		# os.rename(dirname+'/'+fileName, dirname+'/'+new_fileName)

		os.rename(dirname+'/'+fileName, dirname+'/image_0'+str(i)+'.png')
		i = i + 1

change_filename()
