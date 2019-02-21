def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("%s: %s" % (k, v))

def print_everything(*args, **kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s: %s" % (k, v))


#############################
print("1"*50)
print_args("one", "two", "three")
print_args("one", "two", "three", "four")

print_kwargs(name="Jane", surname="Doe")
print_kwargs(age=10)

#############################
print("2"*50)
my_list = ["one", "two", "three"]
print_args(*my_list)

my_dict = {"name": "Jane", "surname": "Doe"}
print_kwargs(**my_dict)

#############################
print("3"*50)
my_dict = {
    "title": "Mr",
    "name": "John",
    "surname": "Smith",
    "formal": False,
    "time": "evening",
}

print(print_everything(**my_dict))
