import officedissector
# import urllib
import urllib.request
from inspect import currentframe, getframeinfo
# from os.path import abspath, dirname
# BASE_PATH = abspath(dirname(__file__))

def myfunc():
	# filepath = "/Users/kim/Downloads/officedissector-master/test/unit_test/testdocs"
	# filename = "/sounds.pptx"
	# file_fullpath = filepath + filename
	# target_url = "https://www.ipa.go.jp/files/000055794.docx"
	# data = urllib.request.urlopen(target_url)
	# for line in data:
	#     print(line.decode('utf-8'))


	#### doc
	target_url = "https://www.ipa.go.jp/files/000055794.docx"
	file_fullpath = urllib.request.urlopen(target_url)
	# doc = urllib.request.urlopen(target_url)
	doc = officedissector.doc.Document(file_fullpath)
	cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
	# print ("doc.is_macro_enabled  :", doc.is_macro_enabled)
	# print ("doc.doc.is_template  :", doc.is_template)

	### mp
	mp = doc.main_part()
	# cf = currentframe(); print("\n[ DEBUG ] [ function ] ",mp, + str(cf.f_code))
	# print("mp.content_type()  :",  mp.content_type())
	# print("mp.name  :", mp.name)

	# xml_contents = (mp.stream().read(10000))

	xml_contents = (mp.stream().read())
	print(xml_contents)

	# file_type = "docx"
	file_type = "pptx"

	if file_type == "docx":
		##### table check
		if "<w:tbl>" in xml_contents:
			print("table!!")
			print("count : ", xml_contents.count("<w:tbl>"))
		else:
			print("no table")

		##### image check 
		if "pic=" in xml_contents:
			print("picture!!")
			print("count : ", xml_contents.count("pic="))
		else:
			print("no picture")

		##### hyperlink check
		if "<w:hyperlink" in xml_contents:
			print("hyperlink!!")
			print("count : ", xml_contents.count("<w:hyperlink"))
		else:
			print("no hyperlink")

		##### header checker
		if "w:headerReference" in xml_contents:
			print("Footnote!!")
			print("count : ", xml_contents.count("w:headerReference"))
		else:
			print("no Footnote")

		##### fotter checker
		if "w:footerReference" in xml_contents:
			print("Footnote!!")
			print("count : ", xml_contents.count("w:footerReference"))
		else:
			print("no Footnote")

		##### textbox checker
		if "<v:textbox" in xml_contents:
			print("textbox!!")
			print("count : ", xml_contents.count("<v:textbox"))
		else:
			print("no textbox")

		##### textbox checker
		if "<v:shape" in xml_contents:
			print("shape!!")
			print("count : ", xml_contents.count("<v:shape"))
		else:
			print("no shape")

myfunc()
