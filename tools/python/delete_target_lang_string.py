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

class Ftrans_checker():

	def __int__(self):
		psss

	def file_cooker(self):

		####  locating target folder by using gui
		root = Tkinter.Tk()
		root.withdraw()
		dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory') 
		print dirname

		####  getting number of files in folder and file name list
		list = os.listdir(dirname)
		# print list ### line for debugging
		number_files = len(list)
		
		m = 0
		while m < number_files:
			if 'docx' in list[m]:
				file_type = 'docx'
				# print file_type

			elif 'xlsx' in list[m]:
				file_type = 'xlsx'
				# print file_type

			elif 'pptx' in list[m]:
				file_type = 'pptx'
				# print file_type

			elif 'txt' in list[m]:
				file_type = 'txt'
				# print file_type

			else:
				pass


		####  show and save the result after deleting target language character

			print '######################################################'
			print '########   '+list[m]+'   ########'
			print '######################################################'

			file_full_path = dirname + '//'+ list[m]
			input_office_text = textract.process(file_full_path, extension=file_type)

			xxx = re.sub(r'[a-z]+', '', input_office_text)
			xxx = re.sub(r'[A-Z]+', '', xxx)
			xxx = re.sub(r'[0-9]+', '', xxx)
			xxx = re.sub(r' ', '', xxx)

			print xxx
			print '######################################################'


			m = m + 1

	def show_result(self):
		# 공통파일을 메모장 또는 브라우저에 열어서 보여준다.
		pass

my_ftrans_checker = Ftrans_checker()
my_ftrans_checker.file_cooker()