class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __repr__(self):
		return '__repr__ for Car'

	def __str__(self):
		return '__str__ for Car'


print("\n"+"-"*10+"  my_car = Car('red', 74937)  "+"-"*10)
my_car = Car('red', 74937)

print("\n"+"-"*10+"  print(my_car)  "+"-"*10)
print(my_car)

print("\n"+"-"*10+"  print('{}'.format(my_car))  "+"-"*10)
print('{}'.format(my_car))

print("\n\n")
