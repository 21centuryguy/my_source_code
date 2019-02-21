class Dog():
	# A somple attemp to model a dog.

	def __init__(self, name, age):
		# Initialize name ane age attributes.
		self.name = name
		self.age = age

	def sit(self):
		# Simulate a dog sitting in response to a command.
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		# Simulate rolling over in response to a command.
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print (my_dog.name)
print (my_dog.age)
my_dog.sit()
my_dog.roll_over()
