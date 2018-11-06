# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup

###################################

# seed_url = 'https://www.intra-mart.jp/'
# seed_url = 'https://www.intra-mart.jp/products/list.html'
# seed_url = 'https://www.intra-mart.jp/case-study/work/004272.html'
seed_url = 'http://www.hamyeondoinda.com/'
# seed_url = 'http://www.navercorp.com/ko/service/business.nhn'
# seed_url = "https://www.daum.net"
# seed_url = "https://www.naver.com"

# base_url = 'https://www.intra-mart.jp/'
# base_url = 'http://www.navercorp.com/'
# base_url = 'https://www.daum.net'
# raw_url_depth_01_path = '/Users/jack/Desktop/raw_url_depth_01.txt'
# handled_url_depth_01_path = '/Users/jack/Desktop/handled_url_depth_01.txt'
# base_url = "https://www.naver.com"
base_url = 'http://www.hamyeondoinda.com/'

###################################

def get_all_link_from_seed_page(seed_url):
	print "###################################"
	print "method : get_raw_url_link_in_seed_page"
	print "----------"

	html = urlopen(seed_url)
	soup = BeautifulSoup(html, "html.parser")

	raw_url_list = []
	for raw_url in soup.find_all('a', href=True):
		raw_url_list.append(raw_url['href'].encode('utf-8'))
	print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

#############

	while seed_url in raw_url_list:
		raw_url_list.remove(seed_url)
	print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	xxx = [raw_url_list.index(i) for i in raw_url_list if 'javascript' in i]
	for m in xxx:
		raw_url_list.pop(m)
	print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	unique_raw_url_list = set(raw_url_list)
	print "unique_raw_url_list : ", len(unique_raw_url_list)
	# for xxx in unique_raw_url_list:print xxx

#############

	handled_url_list = []
	for unique_raw_url in unique_raw_url_list:
		if "http" not in unique_raw_url and "www" not in unique_raw_url:
			handled_url = base_url + str(unique_raw_url)
			# print handled_url
			handled_url_list.append(handled_url)

		elif "http" not in unique_raw_url and "www" in unique_raw_url:
			handled_url = "https:" + str(unique_raw_url)
			# print handled_url
			handled_url_list.append(handled_url)
		else:
			handled_url = str(unique_raw_url)
			# print handled_url
			handled_url_list.append(handled_url)

	handled_url_list = set(handled_url_list)
	handled_url_list = list(handled_url_list)
	print "handled_url_list : ", len(handled_url_list)
	# for xxx in handled_url_list:print xxx

	return handled_url_list


def get_all_link_depth2(seed_url):

	for seed_url in get_all_link_from_seed_page(seed_url):
		print "\n\n\n\n\n\n\n\n\n\n"
		print "####################################"
		print seed_url
		print get_all_link_from_seed_page(seed_url)

get_all_link_depth2(seed_url)

