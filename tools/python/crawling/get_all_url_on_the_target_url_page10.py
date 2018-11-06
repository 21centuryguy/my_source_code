# -*- coding: utf-8 -*-
"""
[ Task ]
1. broken link
2. index link ex) 'https://www.intra-mart.jp/event-seminar/005678.html#pagetop'
3. base url + 상대path --> 분명히 틀리는 경우가 많을 거야
4. 'xxx.html' 외의 확장명으로 끝나는 것들 ex  'xxx.jpg'
"""

# from urllib.request import urlopen ### python3
from urllib import urlopen ### python2
from bs4 import BeautifulSoup
import sys
import codecs

"""  GUI 에서 유알에를 입력하거나 선택하도록 추가 할 것 """
# seed_url_list = ['https://wikileaks.org']
# seed_url_list = ['https://search.wikileaks.org/?q=korea']
# seed_url_list = ['https://www.naver.com']
# seed_url_list = ['http://www.hamyeondoinda.com']
seed_url_list = ['https://www.intra-mart.jp/']
# seed_url_list = ['https://www-en.intra-mart.jp/download/product/forma/programming_guide/texts/pre_processing/index.html']
# seed_url_list = ['https://www.google.com/']
# seed_url_list = ['http://www.tascool.com/']

def get_all_link_from_seed_url_page(seed_url):
	print "###################################"
	###########"
	print "method : get_all_link_from_seed_url_page"
	print "seed_url : ", seed_url
	print "----------------------------------------------"

	html = urlopen(seed_url)
	soup = BeautifulSoup(html, "html.parser")

	html2 = urlopen(seed_url)
	soup2 = BeautifulSoup(html2, "lxml")

	##############################################################################
	##############################################################################
	##############################################################################
	### 검색 패턴을 메소드나 파일로 따로 뺄 것.
	### 검색 패턴을 더 정교하게 만들 것.

	############################################
	### get contents 1 ######################
	"""content = soup2.get_text()
	# content = bytes(content, 'utf-8')
	# content = content.decode('utf-8')
	content = content.splitlines()
	# print type(content)

	for content in content:
		if 'Subject:' in content:
			if 'Korea' in content:
			# if  1 == 1: # 'Korea' in content:				
				print "=================================================================="
				print "=================================================================="
				print content
				print "------------------------------------------------------------------"
				print "\n"
			else:
				pass
		else:
			if 'From:' in content or 'To:' in content or 'Sent:' in content:
				print "=================================================================="
				print "=================================================================="
				print content
				print "------------------------------------------------------------------"
				print "\n"
			else:
				pass"""

	############################################
	### get contents 2 ######################
	"""html2 = urlopen(seed_url)
	soup2 = BeautifulSoup(html2, "lxml.parser")

	content = soup2.find('pre').contents[0]
	print content"""

	############################################
	### get contents t3 ######################
	pre_tag_list = []
	print "***************************** Start line *******************************"
	for pre_tag in soup2.find_all('pre'):
		print pre_tag
		print "\n"

	##############################################################################
	##############################################################################
	##############################################################################
	### get links  ######################

	raw_url_list = []
	for raw_url in soup.find_all('a', href=True):
		raw_url_list.append(raw_url['href'].encode('utf-8'))
	# print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	##############################################################################
	##############################################################################
	##############################################################################
	""" Url 중복 제거  """
	# 현재의 씨드 유알엘 뿐만이 아니라, 이전에 사용한 씨드 유알엘에 대해서도 중복체크 할 것
	## 구체적으로는, 한번 크롤한 씨드 유알엘은 리스트에 다 담아서, 이 리스트를 가지고 중복 제거 할 것


	while seed_url in raw_url_list:
		raw_url_list.remove(seed_url)
	# print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	##############################################################################
	""" 노이즈 제거 및 각 사이트의 유알엘 페턴에 맞춰서 유알엘을 가공하는 기능이 필요 """

	#xxx = [raw_url_list.index(i) for i in raw_url_list if 'javascript' in i]
	#for m in xxx:
	# 	raw_url_list.pop(m)
	# print "raw_url_list : ", len(raw_url_list)
	# for xxx in raw_url_list:print xxx

	print "***************************** Bottom line *******************************"
	unique_raw_url_list = set(raw_url_list)
	print "unique_raw_url_list : ", len(unique_raw_url_list)
	# for xxx in unique_raw_url_list:print xxx

	##############################################################################
	##############################################################################
	##############################################################################

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

	##############################################################################
	##############################################################################
	##############################################################################

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
			print "#### Crawling Depth Count : ", str(i-1), "####"
			print "### URL Crawing Count : ", str(m), "###"
			print len(seed_url_list)
			# print seed_url_list

			try:
				handled_url_list = get_all_link_from_seed_url_page(seed_url)
			except Exception as e:
				print "##############################################"
				print e
				print "A broken link has just skipedd."
				# print "Broken Link Count : ", i
				print"\n\n\n"

			handled_url_list_2.extend(handled_url_list) # +handled_url_list
			print "URLs Count from whole now detph url pages : ",len(handled_url_list_2)
			handled_url_list_3 = list(set(handled_url_list_2))
			print "Uniqe URLs Count from whole now detph url pages : ", len(handled_url_list_3)
			print"\n\n\n"
			m = m + 1

			##############################################################################
			##############################################################################
			##############################################################################
			""" Url 중복 제거 """
			while seed_url in handled_url_list_3:
				handled_url_list_3.remove(seed_url)
			print "handled_url_list_3 after removing seed_url : ", len(handled_url_list_3)
			# for xxx in raw_url_list:print xxx

		if len(handled_url_list_3) != 0:
			global seed_url_list
			seed_url_list = handled_url_list_3
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
