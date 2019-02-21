
class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	"""def __repr__(self):
		return f'Car({self.color!r}, {self.mileage!r})'"""

	def __repr__(self):
		return (f'{self.__class__.__name__}('
			f'{self.color!r}, {self.mileage!r})')

	def __str__(self):
		return f'a {self.color} car'

my_car = Car('red', 74937)

print("\n"+"-"*10+"  print(my_car)  "+"-"*10)
print(my_car)

print("\n"+"-"*10+"  print('{}'.format(my_car))  "+"-"*10)
print('{}'.format(my_car))

print("\n"+"-"*10+"  print(str(my_car))  "+"-"*10)
print(str(my_car))

print("\n\n")

