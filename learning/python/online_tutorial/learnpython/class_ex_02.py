class Vehicle(object):
	name = "default car"
	kind = "car"
	color = "default color"
	value = 100.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		return desc_str

####

car1 = Vehicle()
car1.name = "car1"
car1.color = "car1_color"

car2 = Vehicle()
car2.name = "car2"
car2.color = "car2_color"

###

print(car1.description())
print(car2.description())
