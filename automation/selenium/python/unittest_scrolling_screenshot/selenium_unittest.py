from selenium import webdriver
import unittest
from os.path import abspath, dirname
import time
from time import localtime, strftime

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
		driver = self.driver
		base_url= self.base_url
		driver.set_window_position(0, 0)
		driver.set_window_size(1900, 1100)
		print(driver.get_window_size())

		print("Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime()))
		driver.get(base_url)
		time.sleep(3)
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
