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

class Ftrans_checker():


	def file_cooker(self):

		target_lang = input('Input target langauge (en:1  / ja:2) :')

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

			if target_lang == 1 : ### en
				all_text = re.sub(r'[a-z]+', '', input_office_text) ### remove all alphabets
				all_text = re.sub(r'[A-Z]+', '', all_text) ### remove all capital alphabets
				all_text = re.sub(r'[0-9]+', '', all_text) ### remove all numbers
				all_text = all_text.translate(None, string.punctuation) ### remove all punctuation
				all_text = ''.join(all_text.split()) ### remove all spaces

			elif target_lang == 2 : ### ja
				all_text = re.sub(r'[㐀-䶵一-鿋豈-頻]', '', input_office_text) ### remove all kanji
				all_text = re.sub(r'[あ-ん]+', '', all_text) ### remove all hiragana
				all_text = re.sub(r'[ア-ン]+', '', all_text) ### remove all katakana
				all_text = re.sub(r'[0-9]+', '', all_text) ### remove all numbers
				# all_text = all_text.translate(None, string.punctuation) ### remove all punctuation
				# all_text = ''.join(all_text.split()) ### remove all spaces

			else:
				print 'You should specify target language code (en:1 / ja:2) '
				return False

			print all_text
			print '######################################################'

			m = m + 1


my_ftrans_checker = Ftrans_checker()
my_ftrans_checker.file_cooker()
