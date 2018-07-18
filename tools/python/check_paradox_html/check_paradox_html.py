# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import unittest
import time
import re
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
import bug


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

		print "\n\n\n\n\nTest has Started :", current_data_time

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
		time.sleep(2)  ### It should be changed to waiting method 
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

	print "\n\n\n\n\nTest has Finished :", current_data_time

		# import pdb;pdb.set_trace()
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
