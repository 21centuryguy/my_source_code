from selenium import webdriver
import unittest
from os.path import abspath, dirname
import time
from time import localtime, strftime
from my_modules.get_screenshot import take_screenshots
from inspect import currentframe

BASE_PATH = abspath(dirname(__file__))
# print(BASE_PATH)

class My_test(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(15)
		self.base_url = ["https://www.amazon.com", "https://www.ebay.com"]

	def test_testcase(self):
		cf = currentframe()
		timeinfo_dir = strftime("%Y%m%d_%H%M%S", localtime())
		base_url= self.base_url

		m = 0
		while m < len(base_url):
			key_word_list = ['tablet 2GB ram', 'tablet 4GB ram', 'tablet 8GB ram', 'tablet 16GB ram']

			n = 0
			while n < len(key_word_list):

				### browser setting
				driver = self.driver
				driver.set_window_position(0, 0) ### width, height
				driver.set_window_size(1800, 1200)
				# print(driver.get_window_size())
				# print(driver.get_window_position())

				### url / keyword
				browser_url = base_url[m]
				driver.get(browser_url)
				browser_type = browser_url.replace("https://www.", "")
				key_word = str(key_word_list[n])

				### element locating
				if m == 0:
					textbox = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']") 
				if m == 1:
					textbox = driver.find_element_by_xpath("//*[@id='gh-ac']")

				### operation
				textbox.send_keys(key_word)
				textbox.send_keys(u'\ue007')

				SCROLL_PAUSE_TIME = 0.5
				###### Get scroll height
				last_height = driver.execute_script("return document.body.scrollHeight")
				Y = 0
				# last_height = 0
				while True:
					# Scroll down to bottom
					print("[ DEBUG ] line " + str(cf.f_lineno)+" ==> Y :",Y)
					scroll_scope = 'window.scrollTo(0, window.scrollY + ' + str(Y) + ')'
					driver.execute_script(scroll_scope)
					# Wait to load page
					time.sleep(SCROLL_PAUSE_TIME)
					take_screenshots(driver, BASE_PATH, timeinfo_dir, browser_type, key_word)

					# Calculate new scroll height and compare with last scroll height
					new_height = driver.execute_script("return document.body.scrollHeight")
					if m == 0:
						if new_height > last_height: # new_height == last_height:
							break
					if m == 1:
						if Y < 300:
							if new_height < last_height: # new_height == last_height:
								break
						if Y > 300:
							if new_height == last_height:
								break
					last_height = new_height
					Y = Y + 150

				n = n + 1

			m = m + 1

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return Trueresult_data

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
	"""log_file = BASE_PATH+'/log.txt'
	f = open(log_file, 'w')
	test_start_time = "Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime())
	f.write("\n\n"+"< "*10+str(test_start_time)+" >"*10+"\n\n")
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()"""

