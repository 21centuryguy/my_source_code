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

def extracker():

	########################################################################
	####  locating target folder by using gui

	root = Tkinter.Tk()
	root.withdraw()
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory') 
		# print dirname


	########################################################################
	####  getting number of files in folder and file name list
	list = os.listdir(dirname)
	# print list ### line for debugging
	number_files = len(list)
		
	m = 0
	while m < number_files:

		if 'docx' in list[m]:
			file_type = 'docx'
			# print file_type

			########################################################################
			print '######################################################'
			print '########   '+list[m]+'   ########'
			print '######################################################'

			input_file_full_path = dirname + '/' + list[m]
			print input_file_full_path
			extracted_text = textract.process(input_file_full_path, extension=file_type)

			# print extracted_text

			output_file_full_path = dirname + '/' + list[m]+'.txt'
			print output_file_full_path
			with open(output_file_full_path, 'w') as file:
							file.write(extracted_text)

			print '######################################################'


		elif 'xlsx' in list[m]:
			file_type = 'xlsx'
			# print file_type

			########################################################################
			print '######################################################'
			print '########   '+list[m]+'   ########'
			print '######################################################'

			input_file_full_path = dirname + '/' + list[m]
			print input_file_full_path
			extracted_text = textract.process(input_file_full_path, extension=file_type)

			# print extracted_text

			output_file_full_path = dirname + '/' + list[m]+'.txt'
			print output_file_full_path
			with open(output_file_full_path, 'w') as file:
							file.write(extracted_text)

			print '######################################################'

		elif 'pptx' in list[m]:
			file_type = 'pptx'
			# print file_type

			########################################################################
			print '######################################################'
			print '########   '+list[m]+'   ########'
			print '######################################################'

			input_file_full_path = dirname + '/' + list[m]
			print input_file_full_path
			extracted_text = textract.process(input_file_full_path, extension=file_type)

			# print extracted_text

			output_file_full_path = dirname + '/' + list[m]+'.txt'
			print output_file_full_path
			with open(output_file_full_path, 'w') as file:
							file.write(extracted_text)

			print '######################################################'

		elif 'txt' in list[m]:
			file_type = 'txt'
			# print file_type

			########################################################################
			print '######################################################'
			print '########   '+list[m]+'   ########'
			print '######################################################'

			input_file_full_path = dirname + '/' + list[m]
			print input_file_full_path
			extracted_text = textract.process(input_file_full_path, extension=file_type)

			# print extracted_text

			output_file_full_path = dirname + '/' + list[m]+'.txt'
			print output_file_full_path
			with open(output_file_full_path, 'w') as file:
							file.write(extracted_text)

			print '######################################################'

		else:
			pass;

		m = m + 1
		print m


extracker()