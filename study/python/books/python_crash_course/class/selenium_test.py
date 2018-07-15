class Test():

	def __init__(self, browser, os, version, site_url):
		self.os = os
		self.browser = browser
		self.version = version
		self.site_url = site_url

	def test_info(self):
		print("OS :" + self.os.title())
		print("browser :" + self.browser.title())
		print("Version :" + self.version.title())
		print("Site_url :" + self.site_url)

	def test_01(self):
		print(self.browser + ": Test 1 is running !")

	def test_02(self):
		print(self.browser+ ": Test 2 is running !")


test_chrome = Test('chrome', 'macosx', '46', 'www.xxx.com')
test_ie = Test('ie', 'windows10', '12', 'www.xxx.com')

test_chrome.test_info()
print("\n")
test_ie.test_info()
print("\n")
test_chrome.test_01()
print("\n")
test_ie.test_01()
print("\n")
test_chrome.test_02()
print("\n")
test_ie.test_02()