from selenium import webdriver
import unittest
from os.path import abspath, dirname
import time
from time import localtime, strftime
from my_modules.get_screenshot import take_screenshots

BASE_PATH = abspath(dirname(__file__))
# print(BASE_PATH)

class My_test(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(15)

		self.driver2=webdriver.Chrome()
		self.driver2.implicitly_wait(15)

		self.driver3=webdriver.Chrome()
		self.driver3.implicitly_wait(15)

		self.driver4=webdriver.Chrome()
		self.driver4.implicitly_wait(15)

		self.base_url = "https://www.amazon.com/"


	def test_testcase(self):
		base_url= self.base_url

		driver = self.driver
		driver.set_window_position(0, 0) ### width, height
		driver.set_window_size(900, 550)
		# print(driver.get_window_size())
		# print(driver.get_window_position())
		driver.get(base_url); take_screenshots(driver)
		textbox = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
		textbox.send_keys("python"); take_screenshots(driver)
		searchbutton = driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")
		searchbutton.click(); take_screenshots(driver)

		driver2 = self.driver2
		driver2.set_window_position(910, 0)
		driver2.set_window_size(900, 550)
		# print(driver2.get_window_size())
		# print(driver2.get_window_position())
		driver2.get(base_url); take_screenshots(driver2)
		textbox2 = driver2.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
		textbox2.send_keys("c programming"); take_screenshots(driver2)
		searchbutton2 = driver2.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")
		searchbutton2.click(); take_screenshots(driver2)

		driver3 = self.driver3
		driver3.set_window_position(0, 590)
		driver3.set_window_size(900, 550)
		# print(driver3.get_window_size())
		# print(driver3.get_window_position())
		driver3.get(base_url); take_screenshots(driver3)
		textbox3 = driver3.find_element_by_xpath("//*[@id='twotabsearchtextbox']")		
		textbox3.send_keys("C ++"); take_screenshots(driver3)
		searchbutton3 = driver3.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")
		searchbutton3.click(); take_screenshots(driver3)

		driver4 = self.driver4
		driver4.set_window_position(910, 590)
		driver4.set_window_size(900, 550)
		# print(driver4.get_window_size())
		# print(driver4.get_window_position())
		driver4.get(base_url); take_screenshots(driver4)
		textbox4 = driver4.find_element_by_xpath("//*[@id='twotabsearchtextbox']")		
		textbox4.send_keys("java"); take_screenshots(driver4)
		searchbutton4 = driver4.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")
		searchbutton4.click(); take_screenshots(driver4)

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return Trueresult_data

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	# unittest.main()
	log_file = BASE_PATH+'/log.txt'
	f = open(log_file, 'w')
	test_start_time = "Test has Started :",strftime("%Y-%m-%d %H:%M:%S", localtime())
	f.write("\n\n"+"< "*10+str(test_start_time)+" >"*10+"\n\n")
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

