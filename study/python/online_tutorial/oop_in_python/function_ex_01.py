def my_function():
    my_other_function()

def my_other_function():
    print("Hello!")

# this is fine, because my_other_function is now defined
my_function()

def my_function2():
    my_other_function2()

def my_other_function2():
    # print("Hello!!!")

# this is not fine, because my_other_function2 is not defined yet!
my_function2()
