def show(s):
	showtype = type(s)
	showmethod = dir(s)

	aaa = s

	print aaa

#######################################################
	
	print '#'*200+'\n'

	print [method_name for method_name in dir(aaa)
	 if callable(getattr(aaa, method_name))]

#######################################################

	print '#'*200+'\n'

	print hasattr(aaa,'method')

#######################################################

	print '#'*200+'\n'

	print dir(aaa)

#######################################################

	print '#'*200+'\n'


#######################################################

	print '#'*200+'\n'


show("i am a boy.")

