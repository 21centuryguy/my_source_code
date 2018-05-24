# -*- coding: utf-8 -*-
import unittest, time, re
import codecs
from Tkinter import Tk
import difflib
import os
import shutil
import subprocess
from subprocess import check_output
import textract
from time import localtime, strftime
import sys
import platform
import Tkinter, tkFileDialog
import string
import os

def change_filename():

	root = Tkinter.Tk()
	root.withdraw()
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

	for fileName in os.listdir(dirname):
		# new_fileName = re.sub(r" ?\([^)]+\)", "", fileName)
		new_fileName = re.sub(r" \(", "", fileName)
		new_fileName = re.sub(r"\)", "", new_fileName)
		print new_fileName
		os.rename(dirname+'/'+fileName, dirname+'/'+new_fileName)

change_filename()
