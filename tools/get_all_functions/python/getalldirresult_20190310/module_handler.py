import selenium.webdriver

verified_member_list = []
def module_handler():
	try:
		print('='*100)
		import selenium.webdriver.android
		verified_member_list.append('selenium.webdriver.android')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.blackberry
		verified_member_list.append('selenium.webdriver.blackberry')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.chrome
		verified_member_list.append('selenium.webdriver.chrome')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.common
		verified_member_list.append('selenium.webdriver.common')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.edge
		verified_member_list.append('selenium.webdriver.edge')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.firefox
		verified_member_list.append('selenium.webdriver.firefox')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.ie
		verified_member_list.append('selenium.webdriver.ie')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.opera
		verified_member_list.append('selenium.webdriver.opera')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.phantomjs
		verified_member_list.append('selenium.webdriver.phantomjs')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.remote
		verified_member_list.append('selenium.webdriver.remote')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.safari
		verified_member_list.append('selenium.webdriver.safari')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.support
		verified_member_list.append('selenium.webdriver.support')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver.webkitgtk
		verified_member_list.append('selenium.webdriver.webkitgtk')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	i = open('tmp/tmp.txt', mode='w')
	i.write('')
	for verified_member in verified_member_list:
		i = open('tmp/tmp.txt', mode='a+')
		print('verified_member : ', verified_member)
		i.write(verified_member)
		i.write('\n')
		
	return	verified_member_list

if __name__ == '__main__':
	module_handler()