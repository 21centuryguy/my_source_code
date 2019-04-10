# -*- coding: utf-8 -*-

import sys; reload(sys); sys.setdefaultencoding('utf8')

import pyperclip
import time
import shutil
import os
import datetime
from time import localtime, strftime

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# ---------- global var

# ----- path
# -
clipboard_history_file_full_path = "clipboard_history.txt"
# -
copylist_ref_file_full_path = "/Users/jack/Documents/GitHub/local/build_app/python/py2app/copylist/master/copy_list5.txt"

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# ---------- function definition

# ----------------------------------------------------------------------- 
def remove_dup_in_copylist_ref_file():
	copylist_ref_file_line_list = []
	with open(copylist_ref_file_full_path, "r") as f:
		for line in f:
			copylist_ref_file_line_list.append(line)

	copylist_ref_file_line_list = list(set(copylist_ref_file_line_list))
	copylist_ref_file_line_list.sort()

	with open(copylist_ref_file_full_path, "w") as f:
		for line in copylist_ref_file_line_list:
			f.write("\n")
			f.write(line)

# -----------------------------------------------------------------------
def write_to_clipboard_history_file(current_text_on_clipboard):
	"""
	write to clipboard hisotry file
	"""
	with open(clipboard_history_file_full_path, "a+") as f:
		f.write('\n')
		f.write(current_text_on_clipboard)
	copy_to_copylist_ref_file()
	remove_dup_in_copylist_ref_file()

# -----------------------------------------------------------------------
def copy_to_copylist_ref_file():
	shutil.copy(clipboard_history_file_full_path, copylist_ref_file_full_path)
	# print("Copylist ref file is updated")


# -----------------------------------------------------------------------
def check_new_copy_on_clipboard(current_text_on_clipboard):
	"""
	check new copy on clipboard
	"""

	with open(clipboard_history_file_full_path, "a+") as f:
		if os.path.getsize(clipboard_history_file_full_path) == 0: 
			f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
			f.write(" Start")

	with open(clipboard_history_file_full_path, "r") as f:
		clipboard_history_file_line_list = []
		for clipboard_history_file_line in f:
			clipboard_history_file_line = clipboard_history_file_line.replace("\n", "")
			# print("text on clipboard history : ",clipboard_history_file_line)
			clipboard_history_file_line_list.append(clipboard_history_file_line)


	# --- check check check
	# print("===> clipboard_history_file_line :", clipboard_history_file_line_list)
	# print("===> current_text_on_clipboard :", current_text_on_clipboard)

	tmp = []
	for clipboard_history_file_line in clipboard_history_file_line_list:
		check_position = clipboard_history_file_line.find(">>>")
		clipboard_history_file_line = clipboard_history_file_line[check_position+4:]
		if current_text_on_clipboard == clipboard_history_file_line:
			tmp.append(current_text_on_clipboard)
		else:
			# print("Current_text_on_clipboard is already in clipboard history file")
			pass
	if len(tmp) != 0:
		pass
	else:
		# print("It's new copy !")
		current_text_on_clipboard = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + " [ " + str(len(current_text_on_clipboard)) + " ] >>> " + current_text_on_clipboard
		
		write_to_clipboard_history_file(current_text_on_clipboard)


	# f.close()

# -----------------------------------------------------------------------
def main():

	current_text_on_clipboard = pyperclip.paste()
	while True:
		try:
			current_text_on_clipboard = current_text_on_clipboard.splitlines()
			for current_text_on_clipboard in current_text_on_clipboard:
				if current_text_on_clipboard != None:
					check_new_copy_on_clipboard(current_text_on_clipboard)
				else:
					pass
				current_text_on_clipboard = pyperclip.paste()

		except Exception as e:
			with open("log/err_log.txt", "a+") as f:
				f.write("[ " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + " ] Exception Message : ", e)
				f.write("\n")

		time.sleep(0.1)

		"""
		if "str" in str(type(current_text_on_clipboard)):
			current_text_on_clipboard = current_text_on_clipboard.splitlines()
			for current_text_on_clipboard in current_text_on_clipboard:
				if current_text_on_clipboard != None:
					check_new_copy_on_clipboard(current_text_on_clipboard)
				else:
					pass
				current_text_on_clipboard = pyperclip.paste()
				time.sleep(0.1)
		else:
			print("current_text_on_clipboard : ", type(current_text_on_clipboard))
			print("skipped")

			with open("log/err_log.txt", "a+") as f:
				f.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")) + " >>> " + str(type(current_text_on_clipboard)))
				f.write("\n")
		"""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# ---------- call definition
if __name__ == "__main__":
	main()
