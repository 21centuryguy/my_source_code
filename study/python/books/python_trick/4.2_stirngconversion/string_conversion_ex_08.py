"""
python 2.x
"""

class Car(object):
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __repr__(self):
		return '{}({!r}, {!r})'.format(
			self.__class__.__name__,
			self.color, self.mileage)

	def __unicode__(self):
		return u'a {self.color} car ( mileage : {self.mileage} )'.format(
			self = self)

	def __str__(self):
		return unicode(self).encode('utf-8')


print("\n"+"-"*10+"  my_car = Car('blue', 343243434)  "+"-"*10)
my_car = Car('blue', 343243434)

print("\n"+"-"*10+"  print(repr(my_car))  "+"-"*10)
print(repr(my_car))

print("\n"+"-"*10+"  print(unicode(my_car))  "+"-"*10)
print(unicode(my_car))

print("\n"+"-"*10+"  print('{}'.format(my_car))  "+"-"*10)
print('{}'.format(my_car))

print("\n"+"-"*10+"  print(str(my_car))  "+"-"*10)
print(str(my_car))

print("\n"+"-"*10+"  print(my_car)  "+"-"*10)
print(my_car)

