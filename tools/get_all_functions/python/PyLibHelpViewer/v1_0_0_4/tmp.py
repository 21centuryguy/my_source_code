target = "sklearn"

print("\n\n")

#---------------------------------------------
#--- get package list from 1st result
"""
package_list_from_dpth1_result = []
i = open('result/sklearn_help_text.txt', mode="r")
for text_line in i:
	if "(package)" in text_line:
		text_line = text_line.replace("(package)","") 
		text_line = text_line.replace("\n","")
		text_line = text_line.replace(" ","")
		text_line = target + "." + text_line
		print(text_line)
	else:
		pass
"""

package_list_from_dpth1_result = []
with open('result/sklearn_help_text.txt', mode="r") as file:
	text_line_list = file.read().splitlines()
	# print("="*100)
	# print(text_line_list)
	package_contents_line_number = text_line_list.index("PACKAGE CONTENTS")
	# print(package_contents_line_number)

	edited_text_line_list = []
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
