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

	def test_testcase_1(self):
		driver = self.driver
		base_url= self.base_url
		driver.set_window_position(0, 0)
		driver.set_window_size(900, 550) ### width, height
		print(driver.get_window_size())
		driver.get(base_url)

		time.sleep(10)

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return Trueresult_data

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	# unittest.main()
	log_file = BASE_PATH+'/log.txt'
	f = open(log_file, 'w')
	test_start_time = "Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime())
	f.write("\n\n"+"< "*10+str(test_start_time)+" >"*10+"\n\n")
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()
