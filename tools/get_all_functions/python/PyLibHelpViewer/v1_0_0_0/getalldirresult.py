# import threading; target = "threading"
# import sklearn.neural_network
import selenium.webdriver; target="selenium.webdriver"

def help_target(target):
	"""
	get help(target module) text
	"""
	#---------------------------------------------
	#--- get attr member list from target module
	x = dir(selenium.webdriver) # 변수로 지정하면 변수의 속성들이 찍혀버리네 -_- ;;;;;
	print(x)


	attr_member_list = []
	for xx in x:
		# print(xx)
		attr_member_list.append(xx)
	print("\n")

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
	#---------------------------------------------
	#--- get package list from 1st result
	package_list_from_dpth1_result = []
	i = open("result/result.txt", mode="r")
	for text_line in i:
		# case 1 :  "PACKAGE CONTENTS" 그자체가 또 패키지이면 => "xxx(package)" ex) "chrome (package)"
		# case 2 : "PACKAGE CONTENTS" 그자체가 더 이상 패키지가 아니면 => "xxx" ex) "exceptions"
		# case 1 과  case 2 두 경우 모두 패키지 리스트 가져올 수 있도록 해야 해 !!! 현재는 case 1 밖에 대응이 안돼 !!!
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
	print(package_list_from_dpth1_result)

	return package_list_from_dpth1_result


def import_target(target, package_list):
	"""
	get help(package from help(target module)) text
	"""

	#---------------------------------------------
	#--- generate module importer
	from module_handler_generator import module_handler_generator
	module_handler_generator(target, package_list, 2)

	#---------------------------------------------
	#--- get verified_attr_member_list from module importer
	from module_handler import module_handler
	verified_package_list = module_handler()

	print("="*100)
	print("verified_package_list : ", verified_package_list)
	print("="*100)

	return verified_package_list


def main(mode):
	# target = "selenium"
	# target = "sklearn.neural_network"

	if mode == 1:
		help_target(target)

	elif mode == 2:
		get_target_list(target)

	elif mode == 3:
		package_list = get_target_list(target)
		import_target(target, package_list)

	elif mode == 4:
		i = open("tmp/tmp.txt", mode="r")
		package_list = i.read().splitlines()
		print(package_list)

		#for package in package_list:
		#	help_target(package)
		help_target(package_list)

	else:
		print("No matched option")

#---------------------------------------------
#--- run main

if __name__ == "__main__":
	mode = 3

	main(mode)
