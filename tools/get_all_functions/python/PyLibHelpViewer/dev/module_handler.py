import absl

verified_member_list = []
def module_handler():
	try:
		print('='*100)
		import absl._enum_module
		verified_member_list.append('absl._enum_module')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.app
		verified_member_list.append('absl.app')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.command_name
		verified_member_list.append('absl.command_name')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.flags
		verified_member_list.append('absl.flags')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.logging
		verified_member_list.append('absl.logging')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.testing
		verified_member_list.append('absl.testing')
		print('Import done !')
	except Exception as e:
		print('[ERR] : ', e)

	try:
		print('='*100)
		import absl.third_party
		verified_member_list.append('absl.third_party')
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