import os
import optparse
from getalldirresult import getalldirresult

def write_target_import_line_draft_file():
	i = open("target_import_line_draft.txt", mode="w")
	target_from_cosole  = input("Tyep your target >>> ")
	i.write('import ' + target_from_cosole + '; target ="' + target_from_cosole + '"')

def rewrite_target_import_line_draft_file():
	i = open("target_import_line_draft.txt", mode="w")
	i.write("")
	target_from_cosole  = input("Tyep your target >>>  ")
	i.write('import ' + target_from_cosole + '; target ="' + target_from_cosole + '"')

def read_target_import_line_draft_file():
	i = open("target_import_line_draft.txt", mode="r")
	for current_target in i:
		print("Current target : ", current_target)

def edit_getalldirresult():
	i = open("target_import_line_draft.txt", mode="r")
	for target_import_line in i:
		print(target_import_line)
		
		sep = '='
		target = target_import_line.split(sep)[1:]
		target = target[0]
		target = target.replace('"', '')

		# with is like your try .. finally block in this case
		with open('getalldirresult.py', 'r') as file:
			# read a list of lines into data
			data = file.readlines()

		print(data[18])
		print(data[33])

		# now change the 2nd line, note that you have to add a newline

		data[3] = target_import_line + '\n'
		data[18] =  '\tx = dir(' + target + ')'+ '\n'
		data[33] =  '\t\thelp(' + target + ')'+ '\n'

		# and write everything back
		with open('getalldirresult.py', 'w') as file:
			file.writelines( data )

		def call_getalldirresult(target):
			parser = optparse.OptionParser()

			parser.add_option('-q', '--mode',
				action="store", dest="mode",
				help="mode1: get help text of tareget, mode2: get package list from target, mode3: generate target import line", default="spam")
			options, args = parser.parse_args()
			mode = int(options.mode)
			
			getalldirresult(mode, target)

		call_getalldirresult(target)

# ------------------------
# --- call check_target
def check_target():
	target_import_line_draft_file_size = os.path.getsize("target_import_line_draft.txt")

	if target_import_line_draft_file_size == 0:
		print("target import line file should not be empty !")
		write_target_import_line_draft_file()
		edit_getalldirresult()

	else:
		# read_target_import_line_draft_file()
		# rewrite_target_import_line_draft_file()
		edit_getalldirresult()

#---------------------------------------------
#--- call main

if __name__ == "__main__":
	check_target()
