# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup

base_url = 'https://www.intra-mart.jp/'
seed_url = 'https://www.intra-mart.jp/'
raw_url_depth_01_path = '/Users/jack/Desktop/raw_url_depth_01.txt'
handled_url_depth_01_path = '/Users/jack/Desktop/handled_url_depth_01.txt'

def get_raw_url_link_in_seed_page(seed_url, raw_url_depth_01_path):
	print "###################################"
	print "method : get_raw_url_link_in_seed_page"
	print "----------"

	html = urlopen(seed_url)
	soup = BeautifulSoup(html, "html.parser")

	with open(raw_url_depth_01_path, 'w') as f:
		for url_list in soup.find_all('a', href=True):
			url_list = url_list['href']
			# print url_list
			f.write(url_list)
			f.write("\n")

	with open(raw_url_depth_01_path, 'r') as f:
		url_list = f.read().splitlines()

	while seed_url in url_list:
		url_list.remove(seed_url)
	# print len(url_list)

	raw_url_list = set(url_list)
	print "raw url list count : ", len(raw_url_list)
	print "\n\n\n"
	# print url_list

	return raw_url_list

def get_handled_url_link_in_seed_page(handled_url_depth_01_path, base_url, raw_url_list):
	print "###################################"
	print "method : get_handled_url_link_in_seed_page"
	print "----------"

	with open(handled_url_depth_01_path, 'w') as f:
		for raw_url in raw_url_list:
			if "http" not in raw_url:
				handled_url = base_url + str(raw_url)
			else:
				pass

			f.write(handled_url)
			f.write("\n")

	with open(handled_url_depth_01_path, 'r') as f:
		handled_url_list = f.read().splitlines()	
	
	print "handled url list count : ", len(handled_url_list)
	print "\n\n\n"

	return handled_url_list

raw_url_list = get_raw_url_link_in_seed_page(seed_url, raw_url_depth_01_path)
handled_url_list = get_handled_url_link_in_seed_page(handled_url_depth_01_path, base_url, raw_url_list)

