class ManglingTest:
	def __init__(self):
		self.__mangled = 'hello'

	def get_mangled(self):
		return self.__mangled

m = ManglingTest()

print("-"*50)
try:
	print("m.__mangled")
	print(m.__mangled)
except Exception as e:
	print(e)
print("\n\n\n")

print("-"*50)
try:
	print("m.get_mangled()")
	print(m.get_mangled())
except Exception as e:
	print(e)
print("\n\n\n")



class UnManglingTest:
	def __init__(self):
		self.unmangled = 'hello'

	def get_unmangled(self):
		return self.unmangled

u = UnManglingTest()

print("-"*50)
try:
	print("u.unmangled")
	print(u.unmangled)
except Exception as e:
	print(e)
print("\n\n\n")

print("-"*50)
try:
	print("u.get_unmangled()")
	print(u.get_unmangled())
except Exception as e:
	print(e)
print("\n\n\n")
