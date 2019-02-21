import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    """def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age"""


    def age(self):
        if hasattr(self, "_age"):
        	return self._age

        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
        	age -= 1
        self._age = age
        return age


person = Person(
    "Jane",
    "Doe",
    datetime.date(1977, 11, 21), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

# print(person.name)
# print(person.email)
# print(person.age())
print(person.age())