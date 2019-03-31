import selenium.webdriver

verified_member_list = []
def module_handler():
	try:
		print('='*100)
		import selenium.webdriver.actions
		verified_member_list.append('selenium.webdriver.actions')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

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
		import selenium.webdriver.html5
		verified_member_list.append('selenium.webdriver.html5')
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

	for verified_member in verified_member_list:
		i = open('tmp/tmp.txt', mode='w')
		i.write('') # 일단 먼저 열어서 다 지우고 시작하기
		i = open('tmp/tmp.txt', mode='a+')
		# ==> 이걸 팩키지 리스트를 돌려주는 게 맞을 듯
		# ==> 처음에 임포트 해서 실제 팩키지 직전의 "__package__"를 가져오고 그 다음에 패키지리스트 가져올 수 있는 거라면 --> 단계별로 대응 할 수 있도록 할 것 !!!
		i.write(verified_member)
		i.write('\n')

	return	verified_member_list 


if __name__ == '__main__':
	module_handler()