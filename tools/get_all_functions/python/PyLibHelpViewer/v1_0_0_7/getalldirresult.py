

import os, sys, shutil
import shutil
from tk_tools import tk_tools_main

def init_ref_files():
	i = open("target_import_line_draft.txt", mode="w");i.close()
	i = open("tmp/tmp.txt", mode="w");i.close()
	i = open("result/result.txt", mode="w");i.close()

try:
	import selenium.common.exceptions; target ="selenium.common.exceptions"
except Exception as e:
	print("\n")
	print("="*50)
	print("\n")	
	print("Exception Message : ", e)
	print("Check if the module is valid !")
	print("\n")
	print("="*50)
	print("\n")

	init_ref_files()

def help_target(target):
	"""
	mode 1
	get help(target module) text
	"""

	i = open("target_import_line_draft.txt", mode="r")
	for target_import_line in i:
		exec(target_import_line)

	#---------------------------------------------
	#--- get attr member list from target module
	x = dir(selenium.common.exceptions)
	# print(x)

	attr_member_list = []
	for xx in x:
		# print(xx)
		attr_member_list.append(xx)
	print("\n")

	with open("result/result.txt", "w") as archi:
		t = sys.stdout
		sys.stdout = archi
		help(selenium.common.exceptions)
		sys.stdout = t

	#---------------------------------------------
	#--- generate module importer
	from module_handler_generator import module_handler_generator
	module_handler_generator(target, attr_member_list, 1)

	#---------------------------------------------
	#--- get verified_attr_member_list from module importer
	from module_handler import module_handler
	verified_attr_member_list = module_handler()

	print("="*100)
	print(verified_attr_member_list)
	print("="*100)


def get_target_list(target):
	"""
	mode 2
	"""

	# -------
	result_file_path = "result/result.txt"
	saved_result_file_path = "result/help_docs/" + target + "_help_text.txt"
	shutil.copyfile(result_file_path, saved_result_file_path)

	#---------------------------------------------
	#--- get package list from 1st result
	package_list_from_dpth1_result = []
	with open('result/result.txt', mode="r") as file:
		text_line_list = file.read().splitlines()
		if "PACKAGE CONTENTS" in text_line_list:
			# print("="*100)
			# print(text_line_list)
			package_contents_line_number = text_line_list.index("PACKAGE CONTENTS")
			# print(package_contents_line_number)

			edited_text_line_list = []
			final_text_line_list = []
			text_line = "text_line"
			i = 1
			while len(text_line) > 0:
				# print("count : ", i)
				text_line = text_line_list[package_contents_line_number+i]
				text_line = text_line.replace(" ", "")
				text_line = text_line.replace("(package)","") 
				text_line = text_line.replace("\n","")
				edited_text_line_list.append(text_line)
				# print(text_line)
				i = i + 1

			for text_line in edited_text_line_list:
				text_line = target + "." + text_line
				print(text_line)
				final_text_line_list.append(text_line)

			final_text_line_list.pop(-1)
			package_list_from_dpth1_result = final_text_line_list
			package_list_from_dpth1_result = set(package_list_from_dpth1_result)
			package_list_from_dpth1_result = list(package_list_from_dpth1_result)
			package_list_from_dpth1_result.sort()
			print(">"*7 + " " + "Package List from Target:" + " " + "<"*7)
			print(package_list_from_dpth1_result)
			print("\n")

		else:
			pass
			
		return package_list_from_dpth1_result

def import_target(target, package_list):
	"""
	mode 3
	get help(package from help(target module)) text
	"""

	#---------------------------------------------
	#--- generate module importer
	from module_handler_generator import module_handler_generator
	module_handler_generator(target, package_list, 2)

	#---------------------------------------------
	#--- get verified_attr_member_list from module importer
	from module_handler import module_handler
	verified_package_n_class_list = module_handler()

	# print("="*100)
	# print("verified_package_n_class_list : ", verified_package_n_class_list)
	# print("="*100)

	#---------------------------------------------
	#--- generate and return verified_package_class_list
	verified_package_class_list = []
	for verified_package_class in verified_package_n_class_list:
		target_import_line = verified_package_class
		verified_package_class_list.append(target_import_line)

	print("="*100)
	print("verified_package_class_list :", verified_package_class_list)
	print("="*100)

	# i = open("result/verified_package_class_list.txt", mode="a+")
	i = open("result/verified_package_class_list.txt", mode="w")
	i.write("")
	# i.write("\n\n")
	# i.write("=======\n")
	for target_import_line in verified_package_class_list:
		i.write(target_import_line)
		i.write("\n")
	i.close()

	return verified_package_class_list

#---------------------------------------------
import optparse
parser = optparse.OptionParser()

parser.add_option('-q', '--mode',
	action="store", dest="mode",
	help="mode1: get help text of tareget, mode2: get package list from target, mode3: generate target import line", default="spam")
options, args = parser.parse_args()
mode = int(options.mode)

def getalldirresult(mode, target):
	
	if mode == 1:
		try:
			help_target(target)
		except Exception as e:
			print("="*30)
			print("Exception Message : ", e)
			init_ref_files()

		tk_tools_main(1)		

	elif mode == 2:
		try:
			package_list = get_target_list(target)
			import_target(target, package_list)
			init_ref_files()

		except Exception as e:
			print("="*30)
			print("Exception Message : ", e)
			init_ref_files()
		
		tk_tools_main(2)

	else:
		print("No matched option")
		init_ref_files()

#---------------------------------------------
#--- call main

if __name__ == "__main__":
	getalldirresult(mode, target)
