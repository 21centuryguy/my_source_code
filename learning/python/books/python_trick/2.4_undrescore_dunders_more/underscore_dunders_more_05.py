_MangledGlobal__mangled = 23

class MangledGlobal:
	def test(self):
		return __mangled

m = MangledGlobal()
m2 = MangledGlobal().test()

print(dir(m))
print(m.test())

print(dir(m2))
print(MangledGlobal().test())
