import pyperclip.__main__

verified_member_list = []
def module_handler():
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