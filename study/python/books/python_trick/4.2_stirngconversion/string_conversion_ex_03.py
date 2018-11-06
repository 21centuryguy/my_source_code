"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
4.2 String Conversion(Ebery class Needs a __repr__)
"""

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
