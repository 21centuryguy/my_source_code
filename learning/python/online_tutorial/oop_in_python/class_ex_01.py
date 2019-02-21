import datetime

class Person:
	def __init__(self, name, surname, birthdate, address, telephone, email):
		self.name = name
		self.surname = surname
		self.birthdate = birthdate

		self.address = address
		self.telephone = telephone
		self.email = email		

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year

		print("today : ", today)

		if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
			age -= 1
		return "age :" + str(age)

person = Person(
	"Jane",
	"Doe",
	datetime.date(1977, 11, 21),
	"No. 12 Short Street, Greenvilie",
	"555 456 097",
	"jane.doe@example.com"
)

print(person.name)
print(person.surname)
print(person.birthdate)
print(person.address)
print(person.telephone)
print(person.email)

print(person.age())
