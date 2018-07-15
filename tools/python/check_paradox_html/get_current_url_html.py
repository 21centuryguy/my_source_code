# -*- coding: utf-8 -*-
# from urllib.request import urlopen
from urllib import urlopen
from bs4 import BeautifulSoup


def check_current_page_html(current_url):
	# html = urlopen("https://pre-stg.miraitranslator.com/register/signin.php")
	html = urlopen(current_url)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	# print(bsObj)

	current_url = current_url.replace('https://','')
	current_url = current_url.replace('/','_')
	current_url = current_url.replace('.','_')
	file_full_path = "/Users/kim/Project/local_dev/tool/check_paradox_html/"+current_url+".txt" 
	with open(file_full_path, "w") as f:
		# f.write(file_full_path)
		# f.write("\n\n")
		# f.write(current_url)
		# f.write("\n\n")
		# f.write("="*100)
		# f.write("\n\n")		
		f.write(bsObj.encode('utf-8'))
		f.close()

if __name__ == "__main__":
	pass