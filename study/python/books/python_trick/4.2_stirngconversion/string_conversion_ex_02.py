"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
4.2 String Conversion(Ebery class Needs a __repr__)
"""

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

print("\n\n")
