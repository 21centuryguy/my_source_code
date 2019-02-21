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

print("\n\n")
