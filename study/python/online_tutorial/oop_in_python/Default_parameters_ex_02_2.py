def make_greeting(title, name, surname, formal=True, time=None):
	if formal:
		fullname = "%s %s" % (title, surname)
	else:
		fullname = name

	if time is None:
		greetint = "Hello"
	else:
		greetint = "Good %s" % time

	return "%s, %s!" % (greetint, fullname)

print("\n")
print("#"*50)
print(make_greeting("Mr", "Jack", "Bauer"))
print(make_greeting("Mr", "Jack", "Bauer", False))
print(make_greeting("Mr", "Jack", "Bauer", True, "Night"))

print("\n")
print("#"*50)

print(make_greeting(title="Miss", name="Mary", surname="elizabeth"))
print(make_greeting(title="Miss", name="Mary", surname="elizabeth", formal=False, time="evening"))

print("\n")
print("#"*50)
print(make_greeting("Mr", "John", surname="Smith"))

print("\n")
print("#"*50)
print(make_greeting(surname="Smith", name="John", title="Mr"))
print(make_greeting("Mr", "John", "Smith", time="evening"))
