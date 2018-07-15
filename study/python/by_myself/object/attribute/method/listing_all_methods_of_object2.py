class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
if __name__ == "__main__":
	pass

#######################################################
	
print '\n'+'#'*200+'\n'
print '>>>>>>>   get only method   <<<<<<<'+'\n'
print [method_name for method_name in dir(my_new_car)
if callable(getattr(my_new_car, method_name))]

#######################################################

print '\n'+'#'*200+'\n'
print '>>>>>>>   methond nad variable   <<<<<<<'+'\n'
print dir(my_new_car)

#######################################################

print '\n'+'#'*200+'\n'
print '>>>>>>>   ???   <<<<<<<'+'\n'
print hasattr(my_new_car,"method")

#######################################################

