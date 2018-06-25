class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("restaurant name : ".title()+self.restaurant_name)
		print("cuisine type : ".title()+self.cuisine_type)
		print("number served : ".title()+str(self.number_served))

	def open_restaurant(self):
		print("Welcome !")

	def set_number_served(self, guest_count):
		if guest_count >= self.number_served:
			self.number_served = guest_count
		else:
			print("You can't roll back guest_count !")

	def increment_number_served(self, guest_count):
			self.number_served += guest_count		


restaurant_here = Restaurant('Mana Sickdang', 'Korean')

restaurant_here.describe_restaurant()
restaurant_here.open_restaurant()
print("\n")

restaurant_here.number_served = 5
restaurant_here.describe_restaurant()
print("\n")

restaurant_here.set_number_served(8)
restaurant_here.describe_restaurant()
print("\n")

restaurant_here.increment_number_served(5)
restaurant_here.describe_restaurant()
print("\n")




class User():

	def __init__(self, first_name, last_name, gender, age, food, login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age
		self.food = food
		self.login_attempts = login_attempts

	def describe_user(self):
		print("first_name :".title(), self.first_name)
		print("last_name :".title(), self.last_name)
		print("gender :".title(), self.gender)
		print("age :".title(), self.age)
		print("food :".title(), self.food)
		print("login attempts :".title(), self.login_attempts)

	def increment_login_attemps(self, login_count):
		self.login_attempts += login_count

	def greeting(self):
		print("\nHi,", self.first_name, ", do you want to eat",self.food,"as always?")

	def reset_longin_attempts(self):
		self.login_attempts = 0

user1 = User('Jack', 'kim', 'male', 40, 'noodle', 1)
user2 = User('Marry', 'Lee', 'female', 21, 'apple', 0)
user3 = User('Bill', 'Park', 'male', 35, 'coffe', 3)
user4 = User('Jane', 'Choi', 'female', 58, 'cake', 4)
user5 = User('Michle', 'chang', 'male', 19, 'ice cream', 2)


print("\n\n\n\n========== user1 ==========\n")
user1.greeting()
user1.increment_login_attemps(3)
user1.reset_longin_attempts()
user1.describe_user()

print("\n========== user2 ==========\n")
user2.greeting()
user2.increment_login_attemps(1)
user2.reset_longin_attempts()
user2.describe_user()

print("\n========== user3 ==========\n")
user3.greeting()
user3.increment_login_attemps(8)
user3.reset_longin_attempts()
user3.describe_user()

print("\n========== user4 ==========\n")
user4.greeting()
user4.increment_login_attemps(3)
user4.reset_longin_attempts()
user4.describe_user()


print("\n")
