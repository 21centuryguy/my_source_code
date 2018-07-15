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
from get_current_html import check_current_page_html

class Selenium_unittest_base_code(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		# self.driver=webdriver.Firefox()
		# fp=webdriver.FirefoxProfile(firefox_profile_folder_path);self.driver=webdriver.Firefox(fp) ### check your path
		# self.driver=webdriver.Safari()
		# self.driver=webdriver.Ie('C:\\webdriver\\IEDriverServer.exe') ### check your path
		self.driver.implicitly_wait(15)
		self.base_url = "https://miraitranslator.com"
		self.verificationErrors = []
		self.accept_next_alert = True

	################################################################################################

	def test_selenium_unittest_base_code(self):

		print "\n\n\n\n\nTest has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime())

		driver = self.driver
		driver.maximize_window()
		# driver.set_window_position(0, 0)
		# driver.set_window_size(1650, 1500)
		# driver.maximize_window(); print driver.get_window_size()


	################################

		print "\n\n\n\n\n### [ signin pageのhtmlを読み込んでFileに保存します ] ### "
		driver.get(self.base_url + " ")
		current_url = driver.current_url
		check_current_page_html(current_url)


	################################

		print "\n\n\n\n\n### [ fogot your passworのhtmlを読み込んでFileに保存します ] #### "
		driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)


	################################

		'''print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)

	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)

	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)


	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)


	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)

	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)

	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)'''


	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)

	################################

		print "\n\n\n\n\n#### [ xxxxxのhtmlを読み込んでFileに保存します ] ### "
		# driver.find_element_by_xpath("/html/body/main/form/dl/dd[2]/div/a").click()
		time.sleep(2) ### It should be changed to waiting method 
		current_url = driver.current_url
		check_current_page_html(current_url)







	################################################################################################

		print "\n\n\n\n\nTest has Finished :",strftime("%Y-%m-%d %H:%M:%S", localtime())

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
	f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()))
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()'''