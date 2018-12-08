from selenium import webdriver
import unittest
from os.path import abspath, dirname
import time
from time import localtime, strftime
from inspect import currentframe

BASE_PATH = abspath(dirname(__file__))
print(BASE_PATH)

class TM_handling_group(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(15)
		self.base_url = "https://www.amazon.com/"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_testcase(self):
		cf = currentframe()

		driver = self.driver
		base_url= self.base_url
		driver.set_window_position(0, 0)
		driver.set_window_size(1900, 1100)
		print(driver.get_window_size())

		print("Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime()))
		driver.get(base_url)

		SCROLL_PAUSE_TIME = 0.5

		while True:

			# Get scroll height
			### This is the difference. Moving this *inside* the loop
			### means that it checks if scrollTo is still scrolling 
			last_height = driver.execute_script("return document.body.scrollHeight")
			print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> last_height :",last_height)

			# Scroll down to bottom
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> last_height :",last_height)

			# Wait to load page
			time.sleep(SCROLL_PAUSE_TIME)

			# Calculate new scroll height and compare with last scroll height
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:

				# try again (can be removed)
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

				# Wait to load page
				time.sleep(SCROLL_PAUSE_TIME)

				# Calculate new scroll height and compare with last scroll height
				new_height = driver.execute_script("return document.body.scrollHeight")
				print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> new_height :",new_height)
				print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> last_height :",last_height)

				# check if the page height has remained the same
				if new_height == last_height:
					print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> new_height :",new_height)
					print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> last_height :",last_height)
					# if so, you are done
					break
				# if not, move on to the next loop
				else:
					print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> new_height :",new_height)
					print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> last_height :",last_height)
					last_height = new_height
					continue

		print("Test has Finished :",strftime("%Y-%m-%d %H:%M:%S", localtime()))

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
	"""log_file = BASE_PATH+'/log.txt'
	f = open(log_file, 'a+')
	f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()))
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()"""
