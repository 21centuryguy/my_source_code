import selenium

verified_member_list = []
def module_handler():
	try:
		print('='*100)
		import selenium.common
		verified_member_list.append('selenium.common')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import selenium.webdriver
		verified_member_list.append('selenium.webdriver')
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