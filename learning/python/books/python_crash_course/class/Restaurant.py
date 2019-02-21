class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print("restaurant name : ".title()+self.restaurant_name)
		print("cuisine type : ".title()+self.cuisine_type)

	def open_restaurant(self):
		print("Welcome !")



restaurant_here = Restaurant('Mana Sickdang', 'Korean')
restaurant_there = Restaurant('Susiya', 'Japanese')
restaurant_over_here = Restaurant('Bai xiang lou', 'Chinese')
restaurant_over_there = Restaurant('Jack', 'American')


print("\n========== Restaurant 1 ==========\n")
restaurant_here.describe_restaurant()
restaurant_here.open_restaurant()

print("\n========== Restaurant 2 ==========\n")
restaurant_there.describe_restaurant()
restaurant_there.open_restaurant()

print("\n========== Restaurant 3 ==========\n")
restaurant_over_here.describe_restaurant()
restaurant_over_here.open_restaurant()

print("\n========== Restaurant 4 ==========\n")
restaurant_over_there.describe_restaurant()
restaurant_over_there.open_restaurant()



class User():

	def __init__(self, first_name, last_name, gender, age, food):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age
		self.food = food

	def describe_user(self):
		print("first_name :",self.first_name)
		print("last_name :", self.last_name)
		print("gender :", self.gender)
		print("age :", self.age)
		print("food :", self.food)

	def greeting(self):
		print("\nHi,", self.first_name, ", do you want to eat",self.food,"as always?")

user1 = User('Jack', 'kim', 'male', 40, 'noodle')
user2 = User('Marry', 'Lee', 'female', 21, 'apple')
user3 = User('Bill', 'Park', 'male', 35, 'coffe')
user4 = User('Jane', 'Choi', 'female', 58, 'cake')
user5 = User('Michle', 'chang', 'male', 19, 'ice cream')


print("\n\n\n\n========== user1 ==========\n")
user1.describe_user()
user1.greeting()


print("\n========== user2 ==========\n")
user2.describe_user()
user2.greeting()

print("\n========== user3 ==========\n")
user3.describe_user()
user3.greeting()

print("\n========== user4 ==========\n")
user4.describe_user()
user4.greeting()


print("\n")
