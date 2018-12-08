from selenium import webdriver
from time import localtime, strftime
import distutils.dir_util

def take_screenshots(driver, BASE_PATH, timeinfo_dir, browser_type, key_word):
	timeinfo_file = strftime("%Y%m%d_%H%M%S", localtime())
	screenshot_save_path =  BASE_PATH + "/result/" + timeinfo_dir+ "/"
	# screenshot_save_path =  BASE_PATH + "/result/"
	distutils.dir_util.mkpath(screenshot_save_path)
	screenshot_save_fullpath =  screenshot_save_path + browser_type+"_"+key_word+"_"+timeinfo_file+'.png'
	driver.save_screenshot(screenshot_save_fullpath)
