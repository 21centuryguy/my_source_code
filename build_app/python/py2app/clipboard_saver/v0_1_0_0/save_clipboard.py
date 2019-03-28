# -*- Coding: utf-8 -*-

import pyperclip
import time
import shutil
import os

# ------------------------------
# ---------- global var

# ----- path
# -
clipboard_history_file_full_path = "clipboard_history.txt"
# -
copylist_ref_file_full_path = "/Users/jack/Documents/GitHub/local/build_app/python/py2app/copylist/v0_1_0_3/copy_list5.txt"

# copylist_ref_file_full_path = "/Users/jack/Documents/GitHub/local/build_app/python/py2app/copylist/v0_1_0/copy_list5.txt"

# ------------------------------
# ---------- function definition

# ----- 
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

# ----- 
def write_to_clipboard_history_file(current_text_on_clipboard):
	"""
	write to clipboard hisotry file
	"""
	with open(clipboard_history_file_full_path, "a+") as f:
		f.write('\n')
		f.write(current_text_on_clipboard)
	copy_to_copylist_ref_file()
	remove_dup_in_copylist_ref_file()

# -----
def copy_to_copylist_ref_file():
	shutil.copy(clipboard_history_file_full_path, copylist_ref_file_full_path)
	print("Copylist ref file is updated")


# -----
def check_new_copy_on_clipboard(current_text_on_clipboard):
	"""
	check new copy on clipboard
	"""

	with open(clipboard_history_file_full_path, "a+") as f:
		if os.path.getsize(clipboard_history_file_full_path) == 0: 
			f.write("======== [  ] ========")


	# with open(clipboard_history_file_full_path, "r") as f:
	f = open(clipboard_history_file_full_path, "r")
	print("clipboard history file is open")
	print("f : ", f)

	clipboard_history_file_line_list = []
	for line in f:
		print("text on clipboard history : ",line)
		clipboard_history_file_line_list.append(line)

	print("current_text_on_clipboard check starts")
	if line == current_text_on_clipboard:
		print("Current_text_on_clipboard is already in clipboard history file")
		pass
	else:
		print("It's new copy !")
		write_to_clipboard_history_file(current_text_on_clipboard)

	f.close()

# -----
def main():

	current_text_on_clipboard = pyperclip.paste()
	while True:
		check_new_copy_on_clipboard(current_text_on_clipboard)
		current_text_on_clipboard = pyperclip.paste()
		time.sleep(1)

# ------------------------------
# ---------- call definition
if __name__ == "__main__":
	main()
