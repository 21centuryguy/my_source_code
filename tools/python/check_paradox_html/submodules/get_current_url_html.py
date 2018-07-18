# -*- coding: utf-8 -*-
# from urllib.request import urlopen
from urllib import urlopen
from bs4 import BeautifulSoup
from time import localtime, strftime
from config import *

def get_current_url_html(current_url, current_data_time):
	
	# current_time = strftime("%Y%m%d_%H%M%S", localtime())

	html = urlopen(current_url)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	# print(bsObj)
	print "[ " + current_url + " ] page has been crwaled successfully.\n"

	current_url = current_url.replace('https://','')
	current_url = current_url.replace('/','_')
	current_url = current_url.replace('.','_')
	path_info = pass_path_info(current_data_time)
	file_path_2 = path_info[1]
	file_full_path = file_path_2 + current_url+'.html'
	with open(file_full_path, "w") as f:	
		f.write(bsObj.encode('utf-8'))
		f.close()
		print "[ " + current_url + " ] page has been saved as [ " + file_full_path + " ] successfully.\n"

	# import pdb;pdb.set_trace()

if __name__ == "__main__":
	pass