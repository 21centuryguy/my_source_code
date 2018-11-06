class MangledMethod:
	def __method(self):
		return 42

	def call_it(self):
		return self.__method()


m = MangledMethod()
print("-"*50)
print(dir(m))
print("\n\n\n")

print("-"*50)
try:
	print("m.__method()")
	print(m.__method())
except Exception as e:
	print(e)
print("\n\n\n")

print("-"*50)
try:
	print("_MangledMethod__method()")
	print(_MangledMethod__method())
except Exception as e:
	print(e)
print("\n\n\n")


print("-"*50)
try:
	print("m.call_it()")
	print(m.call_it())
except Exception as e:
	print(e)
print("\n\n\n")