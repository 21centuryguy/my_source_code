"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
4.2 String Conversion(Ebery class Needs a __repr__)
"""

####################################################################
#############################
#############################  class without __str__ or __repr__
#############################
####################################################################

print("\n\n"+"#"*15+"  class Car  "+"#"*15)
class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

print("\n"+"-"*10+"  my_car = Car('red', 37281)  "+"-"*10)
my_car = Car('red', 37281)

print("\n"+"-"*10+"  print(my_car)  "+"-"*10)
print(my_car)
print("\n"+"-"*10+"  print(my_car.color, my_car.mileage)  "+"-"*10)
print(my_car.color, my_car.mileage)


####################################################################
#############################
#############################  class with __str__
#############################
####################################################################

print("\n\n"+"#"*15+"  class Car2  "+"#"*15)
class Car2:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __str__(self):
		return f'a {self.color} car2'

print("\n"+"-"*10+"  my_car2 = Car2('red', 37281)  "+"-"*10)
my_car2 = Car2('red', 37281)

print("\n"+"-"*10+"  print(my_car2)  "+"-"*10)
print(my_car2)
print("\n"+"-"*10+"  print(str(my_car2))  "+"-"*10)
print(str(my_car2))
print("\n"+"-"*10+"  print('{}'.format(my_car2))  "+"-"*10)
print('{}'.format(my_car2))


####################################################################
#############################
#############################  class with __repr__
#############################
####################################################################

print("\n\n"+"#"*15+"  class Car3  "+"#"*15)
class Car3:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __repr__(self):
		return f'a {self.color} car2'

print("\n"+"-"*10+"  my_car3 = Car3('red', 37281)  "+"-"*10)
my_car3 = Car3('red', 37281)

print("\n"+"-"*10+"  print(my_car3)  "+"-"*10)
print(my_car3)
print("\n"+"-"*10+"  print(repr(my_car3))  "+"-"*10)
print(repr(my_car3))
print("\n"+"-"*10+"  print('{}'.format(my_car3))  "+"-"*10)
print('{}'.format(my_car3))

print("\n\n")
