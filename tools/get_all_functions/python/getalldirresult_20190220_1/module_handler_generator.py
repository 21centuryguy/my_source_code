import os
current_path = os.path.abspath(__file__)


def module_handler_generator(target, member_list, mode):
	"""
	target
	member_list
	mode => 1 : help / 2 : import
	"""

	verified_member_list = []
	### open file
	filefullpath = "module_handler.py"
	f = open(filefullpath, "w+")
	f.write("import " + target)
	f.write("\n\n")
	f.write("verified_member_list = []")
	f.write("\n")
	f.write("def module_handler():")
	f.write("\n")

	for member in member_list:

		if mode == 1: # help 
			expression = "help(" + target + "." + member + ")" ### target.package에 대한 help는 따로 구분 필요
		if mode == 2: # import
			expression = "import " + member

		f.write("\t")
		f.write("try:")
		f.write("\n")
		f.write("\t\t")
		f.write("print('='*100)")
		f.write("\n")
		f.write("\t\t")
		f.write(expression)
		f.write("\n")
		f.write("\t")
		f.write("\t")
		f.write("verified_member_list.append("+"'"+member+"'"+")")
		f.write("\n")
		f.write("\t\t")

		if mode == 1: # help 
			f.write("print('[OK] Hlep is printed !')")
		if mode == 2: # import
			f.write("print('Import done !')")
		f.write("\n")
		f.write("\t")
		f.write("except Exception as e:")
		f.write("\n")
		f.write("\t\t")
		f.write("print('[ERR] : ', e)")
		f.write("\n\n")

	### wreite line in tmp.txt
	f.write("\t")
	f.write("for verified_member in verified_member_list:")
	f.write("\n")
	f.write("\t\t")
	f.write("i = open('tmp/tmp.txt', mode='w')")
	f.write("\n")
	f.write("\t\t")
	f.write("i.write('')")
	f.write("\n")
	f.write("\t\t")
	f.write("i = open('tmp/tmp.txt', mode='a+')")
	f.write("\n")
	f.write("\t\t")
	f.write("i.write(verified_member)")
	f.write("\n")
	f.write("\t\t")
	f.write("i.write('\\n')")
	f.write("\n")
	f.write("\t\t")

	### write import line
	f.write("\n")
	f.write("\t")
	f.write("return")
	f.write("\t")
	f.write("verified_member_list")

	### wreite return line
	f.write("\n\n")
	f.write("if __name__ == '__main__':")
	f.write("\n")
	f.write("\t")
	f.write("module_handler()")
