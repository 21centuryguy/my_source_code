# -*- coding: utf-8 -*-
import re
import os
import tkinter, tkinter.filedialog

def change_filename():

	root = tkinter.Tk()
	root.withdraw()
	dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

	for fileName in os.listdir(dirname):
		# new_fileName = re.sub(r" ?\([^)]+\)", "", fileName)
		new_fileName = re.sub(r"aaa", "bbb", fileName)
		print(new_fileName)
		os.rename(dirname+'/'+fileName, dirname+'/'+new_fileName)

change_filename()
