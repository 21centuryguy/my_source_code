# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import codecs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Tkinter import Tk
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
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Crawl_the_webo_with_selenium(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.wikipedia.org"
		self.verificationErrors = []
		self.accept_next_alert = True


	def test_crawl_the_webo_with_selenium(self):


############### preparing tools ###############

	############### tool 1 : crawl_wep_page ###############

		def crawl_wep_page(current_url):
			html = urlopen(current_url)
			bsObj = BeautifulSoup(html.read(), "html.parser")
			print(bsObj)

			crawled_html_file_full_path = "/Users/jack/Desktop/" + current_url.replace(':','').replace('//','/').replace('/','_') + strftime("%Y%m%d_%H%M%S", localtime()) + ".txt"
			with open(crawled_html_file_full_path, 'w') as f:
				f.write(str(bsObj))
				f.close()


#############################################################################
#############################################################################
############################## start operation ##############################

	############################################################
	############### operation 1 : access base url ###############
		driver = self.driver
		driver.set_window_position(0, 0)
		driver.get(self.base_url + " ")
		# driver.maximize_window() 
		# driver.set_window_size(1300, 1100)
		# print driver.get_window_size()
		time.sleep(1)
		current_url = driver.current_url
		print (driver.current_url)

		############### get current page html  ###############
		crawl_wep_page(driver.current_url)


	####################################################################################
	###############  operation 2 :  move to 'python' search result page  ###############

		driver.find_element_by_xpath("//*[@id='searchInput']").clear()
		driver.find_element_by_xpath("//*[@id='searchInput']").send_keys("python")
		driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button/i").click()


		############### get current page html  ###############
		crawl_wep_page(driver.current_url)


	############################################################
	###############  operation x :  xxxxx  ###############

		# driver.find_element_by_xpath("xxx").xxx()


		############### get current page html  ###############
		# crawl_wep_page(driver.current_url)



	############################################################
	###############  operation x :  xxxxx  ###############

		# driver.find_element_by_xpath("xxx").xxx()


		############### get current page html  ###############
		# crawl_wep_page(driver.current_url)



	############################################################
	###############  operation x :  xxxxx  ###############

		# driver.find_element_by_xpath("xxx").xxx()


		############### get current page html  ###############
		# crawl_wep_page(driver.current_url)




##############################################################

		print ("Test has Finished :",strftime("%Y-%m-%d %H:%M:%S", localtime()))	

##############################################################

	print ("Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime()))

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

if __name__ == "__main__":
	unittest.main()
	'''log_file = semi_log_path+'text_mado_trans_group_semi_log.txt'
	exec write_semi_log # f = open(log_file, 'w')
	f.write(test_info_description)
	f.write("Test End :\n")
	f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()))
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()'''