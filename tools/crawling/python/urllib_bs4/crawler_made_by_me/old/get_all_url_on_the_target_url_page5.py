# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup

seed_url_list = ['https://www.intra-mart.jp/']

def get_all_link_from_seed_url_page(seed_url):
	print "###################################"
	###########"
	print "method : get_all_link_from_seed_url_page"
	print "seed_url : ", seed_url
	print "----------"

	html = urlopen(seed_url)
	soup = BeautifulSoup(html, "html.parser")

	raw_url_list = []
	for raw_url in soup.find_all('a', href=True):
		raw_url_list.append(raw_url['href'].encode('utf-8'))
	print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	#######################################

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

	#######################################

	handled_url_list = []
	for unique_raw_url in unique_raw_url_list:
		if "http" not in unique_raw_url and "www" not in unique_raw_url:
			handled_url = seed_url + str(unique_raw_url)
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

	#######################################

	return handled_url_list

	#######################################


def main():
	print "method : main"

	i = 1
	while True:
		m = 1
		for seed_url in seed_url_list:
			print "#### Crawling Depth Count : ", str(i), "####"
			print "### URL Crawing Count : ", str(m), "###"
			print len(seed_url_list)
			# print seed_url_list
			handled_url_list = get_all_link_from_seed_url_page(seed_url)
			# print handled_url_list
			# print 111111
			# print type(handled_url_list)
			# print len(handled_url_list)
			print"\n\n\n"
			m = m + 1

		if len(seed_url_list) != 0:
			# print 22222222
			# print type(seed_url_list)
			# print len(seed_url_list)
			# print seed_url_list
			global seed_url_list
			seed_url_list = handled_url_list
			# print 33333333
			# print type(seed_url_list)
			# print len(seed_url_list)
			# print seed_url_list
			print "### Global variable chagne count : ", i, "###"


		else:
			print"\n\n\n"
			print "There is no more link -_-;" 
			break
			
		i = i + 1

main()