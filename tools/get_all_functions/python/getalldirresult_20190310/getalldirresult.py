import os
import sys
import shutil
import selenium.webdriver; target ="selenium.webdriver"

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
	x = dir(selenium.webdriver)
	# print(x)

	attr_member_list = []
	for xx in x:
		# print(xx)
		attr_member_list.append(xx)
	print("\n")

	with open("result/result.txt", "w") as archi:
		t = sys.stdout
		sys.stdout = archi
		help(selenium.webdriver)
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
	saved_result_file_path = "result/" + target + "_help_text.txt"
	shutil.copyfile(result_file_path, saved_result_file_path)

	# -------

	#---------------------------------------------
	#--- get package list from 1st result
	package_list_from_dpth1_result = []

	i = open('result/result.txt', mode="r")
	for text_line in i:
		if "(package)" in text_line:
			text_line = text_line.replace("(package)","") 
			text_line = text_line.replace("\n","")
			text_line = text_line.replace(" ","")
			text_line = target + "." + text_line
			# print(text_line)
			package_list_from_dpth1_result.append(text_line)
		else:
			pass

	package_list_from_dpth1_result = set(package_list_from_dpth1_result)
	package_list_from_dpth1_result = list(package_list_from_dpth1_result)
	package_list_from_dpth1_result.sort()
	print(">"*7 + " " + "Package List from Target:" + " " + "<"*7)
	print(package_list_from_dpth1_result)
	print("\n")

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

	print("="*100)
	print("verified_package_n_class_list : ", verified_package_n_class_list)
	print("="*100)

	#---------------------------------------------
	#--- generate and return verified_package_class_list
	verified_package_class_list = []
	for verified_package_class in verified_package_n_class_list:
		target_import_line = verified_package_class
		# target_import_line = 'import ' + verified_package_class + '; target ="' + verified_package_class + '"'
		verified_package_class_list.append(target_import_line)

	print("="*100)
	print("verified_package_class_list :", verified_package_class_list)
	print("="*100)

	i = open("result/verified_package_class_list.txt", mode="a+")
	i.write("")
	i.write("\n\n")
	i.write("=======\n")
	for target_import_line in verified_package_class_list:
		i.write(target_import_line)
		i.write("\n")
	i.close()

	return verified_package_class_list


def init_ref_files():
	i = open("target_import_line_draft.txt", mode="w");i.close()
	i = open("tmp/tmp.txt", mode="w");i.close()
	i = open("result/result.txt", mode="w");i.close()



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
		help_target(target)

	elif mode == 2:
		package_list = get_target_list(target)
		import_target(target, package_list)
		init_ref_files()

	# elif mode == 2:
	# get_target_list(target)

	else:
		print("No matched option")
		init_ref_files()

#---------------------------------------------
#--- call main

if __name__ == "__main__":
	getalldirresult(mode, target)
