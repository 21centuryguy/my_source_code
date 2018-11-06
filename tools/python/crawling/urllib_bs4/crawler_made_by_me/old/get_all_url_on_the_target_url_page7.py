# -*- coding: utf-8 -*-
"""
[ 落し穴 ]

1. broken link

"""

# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup


"""  GUI 에서 유알에를 입력하거나 선택하도록 추가 할 것 """
# seed_url_list = ['https://wikileaks.org']
# seed_url_list = ['https://www.naver.com']
# seed_url_list = ['http://www.hamyeondoinda.com']
seed_url_list = ['https://www.intra-mart.jp/']
# seed_url_list = ['https://www.google.com/']


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

	#######################################
	#######################################
	#######################################
	""" 노이즈 제거 및 각 사이트의 유알엘 페턴에 맞춰서 유알엘을 가공하는 기능이 필요 """


	#xxx = [raw_url_list.index(i) for i in raw_url_list if 'javascript' in i]
	#for m in xxx:
	# 	raw_url_list.pop(m)
	print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	unique_raw_url_list = set(raw_url_list)
	print "unique_raw_url_list : ", len(unique_raw_url_list)
	# for xxx in unique_raw_url_list:print xxx

	#######################################
	#######################################
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
	#######################################
	#######################################
	""" 획득한 각각의 유알엘 개별적으로 뷰티플스프를 이용해서 필요한 정보를 가져오는 기능을 추가 """


	#######################################
	#######################################
	#######################################



	return handled_url_list

	#######################################

def main():
	print "method : main"

	i = 1
	while True:
		m = 1
		handled_url_list_2 = []
		handled_url_list_3 = []
		for seed_url in seed_url_list:
			print "#### Crawling Depth Count : ", str(i), "####"
			print "### URL Crawing Count : ", str(m), "###"
			print len(seed_url_list)
			# print seed_url_list
			handled_url_list = get_all_link_from_seed_url_page(seed_url)
			handled_url_list_2.extend(handled_url_list) # +handled_url_list
			print "URLs Count from whole now detph url pages : ",len(handled_url_list_2)
			handled_url_list_3 = list(set(handled_url_list_2))
			print "Uniqe URLs Count from whole now detph url pages : ", len(handled_url_list_3)
			# print handled_url_list
			# print 111111
			# print type(handled_url_list)
			# print len(handled_url_list)
			print"\n\n\n"
			m = m + 1

		if len(handled_url_list_3) != 0:
			# print 22222222
			# print type(seed_url_list)
			# print len(seed_url_list)
			# print seed_url_list
			global seed_url_list
			seed_url_list = handled_url_list_3
			# print 33333333
			# print type(seed_url_list)
			# print len(seed_url_list)
			# print seed_url_list
			print "##############################################"
			print "##############################################"
			print "##############################################"
			print "### Global variable chagne count : ", i, "###"


		else:
			print"\n\n\n"
			print "There is no more link -_-;" 
			break

		i = i + 1

main()