########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
### folder structure

'''
(py35) jack (dev *) check_paradox_html
$ tree
.
├── check_paradox_html.py
├── crawled_html_files
│   ├── 20180716_180727
│   │   ├── en_wikipedia_org_wiki_Python.html
│   │   └── www_wikipedia_org_.html
│   ├── 20180716_180930
│   │   ├── en_wikipedia_org_wiki_Python.html
│   │   └── www_wikipedia_org_.html
│   └── diff_result
│       └── diff\ 20180716_180930_\ 20180716_180727
│           ├── \ 20180716_180930-\ 20180716_180727_en_wikipedia_org_wiki_Python.html_diff_resutl.txt
│           └── \ 20180716_180930-\ 20180716_180727_www_wikipedia_org_.html_diff_resutl.txt
├── get_current_url_html.pyc
└── submodules
    ├── __init__.py
    ├── config.py
    ├── diff_that_damnit.py
    └── get_current_url_html.py

6 directories, 12 files
(py35) jack (dev *) check_paradox_html

'''



########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
####### check_html.py
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import unittest, time, re
import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tkinter import Tk
import difflib
import os
import shutil
import subprocess
from subprocess import check_output
import textract
# import slate
from time import localtime, strftime
import sys
import platform
from submodules import get_current_url_html
from submodules import diff_that_damnit
from submodules import config

class Selenium_unittest_base_code(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		# self.driver=webdriver.Firefox()
		# fp=webdriver.FirefoxProfile(firefox_profile_folder_path);self.driver=webdriver.Firefox(fp) ### check your path
		# self.driver=webdriver.Safari()
		# self.driver=webdriver.Ie('C:\\webdriver\\IEDriverServer.exe') ### check your path
		self.driver.implicitly_wait(15)
		# self.base_url = "https://miraitranslator.com"
		self.base_url = "https://www.wikipedia.org"
		self.verificationErrors = []
		self.accept_next_alert = True

	################################################################################################

	def test_selenium_unittest_base_code(self):

		current_data_time = strftime("%Y%m%d_%H%M%S", localtime())

		print "\n\n\n\n\nTest has Started :",current_data_time

		driver = self.driver
		driver.maximize_window()
		# driver.set_window_position(0, 0)
		# driver.set_window_size(1650, 1500)
		# driver.maximize_window(); print driver.get_window_size()
		driver.get(self.base_url + " ")

	################################

		print "\n\n\n\n\n[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"
		print "      [[[[[[[  Current url page html crwaling  ]]]]]]]            \n"
		print "[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		current_url = driver.current_url
		get_current_url_html.get_current_url_html(current_url, current_data_time)


		################################

		driver.find_element_by_xpath("//*[@id='searchInput']").clear()
		driver.find_element_by_xpath("//*[@id='searchInput']").send_keys("python")
		driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button/i").click()

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html.get_current_url_html(current_url, current_data_time)


	################################

		'''print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### " "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)


	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)


	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)


	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)

	################################

		print "\n\n\n\n\n### Getting and saving whole html of [ " + driver.current_url + " ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		get_current_url_html(current_url)'''

		diff_that_damnit.diff_that_damnit(current_data_time)

	################################################################################################

		print "\n\n\n\n\nTest has Finished :",current_data_time

	################################################################################################

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return Trueresult_data

	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

################################################################################################

if __name__ == "__main__":
	unittest.main()
	'''log_file = semi_log_path+'log.txt' ### check your path
	f = open(log_file, 'w')
	f.write("Test End :\n")
	f.write(current_data_time))
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()'''
	


########################################################################
########################################################################
########################################################################
########################################################################
########################################################################

####### config.py
# -*- coding: utf-8 -*-
import distutils.dir_util

def pass_path_info(current_data_time):
	folder_path_2 = "/Users/jack/gitlocal/tools/python/check_paradox_html/crawled_html_files/"+current_data_time+"/"
	distutils.dir_util.mkpath(folder_path_2)
	
	folder_path_1 = "/Users/jack/gitlocal/tools/python/check_paradox_html/crawled_html_files/"
	
	return folder_path_1, folder_path_2

if __name__ == "__main__":
	pass




########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
####### get_current_url_html
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

if __name__ == "__main__":
	pass




########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
####### diff_that_damnit.py

# -*- coding: utf-8 -*-
import os
import Tkinter, tkFileDialog
from config import *
import difflib
import distutils.dir_util

def diff_that_damnit(current_data_time):





########################################################################
########################################################################
########################################################################
########################################################################
########################################################################
##### select before and after folder and get file list
	root = Tkinter.Tk()
	root.withdraw()

#####################################################

	def select_folder_and_get_file_list():
		######################################################################
		##### select before folder and get file list
		##### select before folder
		print "\n\n\n>"
		print "=>"
		print "==>>"
		print "===>>>"
		print "====>>>>"
		print "=====>>>>>   Please select [ Befre folder ] for checking html diff status from OS UI.\n\n\n"

		before_folder_path = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
		file_list_in_before_folder = os.listdir(before_folder_path)
		file_list_in_before_folder.sort()
		file_list_in_before_folder

		##### get file list
		file_count = len(file_list_in_before_folder)
		print "\n\n============ [ before folder path and file list ] ============"
		print "\nBefore folder path :",before_folder_path 
		print "\nFile list in the before folder :", file_list_in_before_folder
		print "\nTotal file count :", file_count


		######################################################################
		##### select after folder and get file list
		##### select after folder
		path_info = pass_path_info(current_data_time)
		folder_path_1 = path_info[0]
		folder_list_in_the_crawled_html_files = os.listdir(folder_path_1)
		folder_list_in_the_crawled_html_files.sort()
		folder_list_in_the_crawled_html_files.pop(0) ### delete '.DS_Store'
		folder_list_in_the_crawled_html_files.pop(-1) ### delete 'diff_result'
		# print folder_list_in_the_crawled_html_files

		last_folder_in_the_crawled_html_files = folder_list_in_the_crawled_html_files[-1]
		last_folder_in_the_crawled_html_files_path = folder_path_1 + last_folder_in_the_crawled_html_files

		##### get file list
		file_list_in_the_last_folder = os.listdir(last_folder_in_the_crawled_html_files_path)
		file_list_in_the_last_folder.sort()
		file_count = len(file_list_in_the_last_folder)
		print "\n\n============ [ after folder path and file list ] ============"
		print "\nLast folder path :", last_folder_in_the_crawled_html_files_path
		print "\nFile list in the last folder :", file_list_in_the_last_folder
		print "\nTotal file count :", file_count	

		return before_folder_path, file_list_in_before_folder, file_count, last_folder_in_the_crawled_html_files_path, file_list_in_the_last_folder




	def compare_before_and_after_folder(*arg):
		######################################################################
		##### diff each file in before folder and after folder

		print "\n\n\n\n\n[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"
		print "            [[[[[[[  Diff checking  ]]]]]]]            \n"
		print "[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]\n"
		m = 0
		while m < file_count:

			############### diff one by one ###############
			before_file_full_path = before_folder_path + "/" + file_list_in_before_folder[m]
			after_file_full_path = last_folder_in_the_crawled_html_files_path + "/" + file_list_in_the_last_folder[m]

			print "\n\n============ [ " + str(m+1) + "th before file ] ============\n"
			print before_file_full_path

			print "\n\n============ [ " + str(m+1) + "th after file ] ============\n"
			print after_file_full_path

			with open(before_file_full_path) as before, open(after_file_full_path) as after:
				diff = difflib.context_diff(before.readlines(), after.readlines())
			
			############### save diff result ###############
			path_info = pass_path_info(current_data_time)
			folder_path_1 = path_info[0]

			before_folder_name = before_folder_path.replace(folder_path_1, ' ')
			after_folder_name = last_folder_in_the_crawled_html_files_path.replace(folder_path_1, ' ')
			before_file_name = file_list_in_before_folder[m].replace(folder_path_1, ' ')
			after_file_name = file_list_in_the_last_folder[m].replace(folder_path_1, ' ')

			diff_result_folder_path = folder_path_1 + "/diff_result/" +"diff"+ before_folder_name +"_"+ after_folder_name
			distutils.dir_util.mkpath(diff_result_folder_path)
			diff_result_fullpath = diff_result_folder_path +"/"+ before_folder_name+"-"+after_folder_name +"_"+ file_list_in_before_folder[m]+"_diff_resutl.txt"		
			with open(diff_result_fullpath, 'w') as diff_result:
				for line in diff:
					diff_result.write(line)

			############### report diff result ###############

			diff_result_size = os.path.getsize(diff_result_fullpath)
			
			if diff_result_size == 0: 
				print "\n>"
				print "=>"
				print "==>>"
				print "===>>>"
				print "====>>>>"
				print "=====>>>>>   [ Diff checking count : " + str(m+1)+" ] : [ "+ before_folder_name +"_"+ before_file_name +" ]"+ " and " + "[ "+ after_folder_name +"_"+ after_file_name + " ] is >>>>>>> SAME <<<<<<<.\n\n"

			else:
				print "\n>"
				print "=>"
				print "==>>"
				print "===>>>"
				print "====>>>>"				
				print "=====>>>>>   [ Diff checking count : " + str(m+1)+" ] : [ "+ before_folder_name +"_"+ before_file_name +" ]"+ " and " + "[ "+ after_folder_name +"_"+ after_file_name + " ] is >>>>>>> NOT SAME <<<<<<<.\n\n"
			m = m + 1

######################################################################
	xxx = select_folder_and_get_file_list()
	xxx = list(xxx)
	before_folder_path = xxx[0]
	file_list_in_before_folder = xxx[1]
	file_count = xxx[2]
	last_folder_in_the_crawled_html_files_path = xxx[3]
	file_list_in_the_last_folder = xxx[4]

	compare_before_and_after_folder(before_folder_path, file_list_in_before_folder, file_count, last_folder_in_the_crawled_html_files_path, file_list_in_the_last_folder)

######################################################################

if __name__ == "__main__":
	pass


########################################################################
########################################################################
########################################################################
########################################################################
########################################################################


