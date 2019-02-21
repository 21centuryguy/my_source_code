class Test:
	def __init__(self):
		self.foo = 11
		self._bar  =23
		self.__baz = 42

class ExtendedTest(Test):
	def __init__(self):
		super().__init__()
		self.foo = 'overridden'
		self._bar = 'overridden'
		self.__baz = 'overridden'

t = Test()
t2 = ExtendedTest()

try:
	print("\n\n\n")
	print("="*50)
	print("objects_1 = [t, dir(t), t2, dir(t), t2.foo, t2._bar]")
	objects_1 = [t, dir(t), t2, dir(t), t2.foo, t2._bar]
except Exception as e:
		print("-_-; "*50)
		print(e)
		pass

try:
	print("\n\n\n")
	print("="*50)
	print("objects_2 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2.__baz]")
	objects_2 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2.__baz]
except Exception as e:
		print("-_-; "*20)		
		print(e)
		pass

try:
	print("\n\n\n")
	print("="*50)
	print("objects_3 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2._Test__baz]")
	objects_3 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2._Test__baz]
except Exception as e:
		print("-_-; "*50)		
		print(e)
		pass

try:
	print("\n\n\n")
	print("="*50)
	print("objects_4 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2._ExtendedTest__baz]")
	objects_4 = [t, dir(t), t2, dir(t), t2.foo, t2._bar, t2._ExtendedTest__baz]
except Exception as e:
		print("-_-; "*50)		
		print(e)
		pass

i = 1
while i < 5 : 
	print("\n\n\n")
	print("="*50)
	print("objects_"+str(i))

	try:
		for xxx in eval("objects_"+str(i)):
			print("-"*30)
			print(xxx)
	except Exception as e:
			print("-_-; "*20)		
			print(e)
			pass
	i = i + 1
