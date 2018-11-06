import string
import random
import strgen

def pw_gen(size, generator_condition):
	generated_random_string = ''.join(random.choice(generator_condition) for _ in range(size))
	if any(char.isdigit() for char in generated_random_string) == True:
		return generated_random_string
	else:
		print("#"*30,"\nNo number :", generated_random_string,"\nRegenerate random string.") 
		while any(char.isdigit() for char in generated_random_string) == False:
			generated_random_string = ''.join(random.choice(generator_condition) for _ in range(size))
			return generated_random_string

def random_generator():
	generated_random_string = strgen.StringGenerator("[\d\w]{12}").render()
	return generated_random_string

if __name__ == "__main__":
	print("#"*30,"\npw_gen : ", pw_gen(8, string.ascii_lowercase + string.digits + string.ascii_uppercase),"\n")
	print("#"*30,"\nrandom_generator : ", random_generator(),"\n")































"""
print("This code executes before main.") 

def functionA():
    print("Function A")

def functionB():
    print("Function B")

if __name__ == '__main__':
    # functionA()
    # functionB()
    pass
"""


"""
def pw_gen(size = 16, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))
print(pw_gen(16))
"""

"""
def random_string_generator(generator_condition, string_digit):
	generated_random_string = ''.join(random.choice(generator_condition) for _ in range(string_digit))
	while any(char.isdigit() for char in generated_random_string) == False:
		generated_random_string = ''.join(random.choice(generator_condition) for _ in range(string_digit))
		print(generated_random_string)
		time.sleep(0.2)
	print(generated_random_string)


while True:
	random_string_generator("string.ascii_uppercase + string.ascii_lowercase + string.digits", 12)
"""

"""
def random_string_generator(generator_condition, string_digit):
	print(generator_condition)
	generated_random_string = ''.join(random.choice(generator_condition) for _ in range(string_digit))
	print(generated_random_string)

while True:
	# random_string_generator('string.digits + string.ascii_uppercase + string.ascii_lowercase', 10)
	random_string_generator('string.digits', 10)
	time.sleep(1)
"""

"""
while True:
	generated_random_string = ''.join(random.choice(string.digits) for _ in range(10))
	generated_random_string = ''.join(random.choice(string.digits) for _ in range(10))
	generated_random_string = ''.join(random.choice(string.digits) for _ in range(10))	
	print(generated_random_string)
"""


"""
def random_string_generator(string_digit):
	# generated_random_uppercase_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(string_digit))
	# generated_random_lowercase_string = ''.join(random.choice(string.ascii_uppercase) for _ in range(string_digit))
	generated_random_int_number = ''.join(random.choice(string.digits) for _ in range(string_digit))
	# print(generated_random_uppercase_string+generated_random_lowercase_string+str(generated_random_int_number))
	print(generated_random_int_number)

while True:
	random_string_generator(3)
	time.sleep(0.3)
"""

"""
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = 7
p =  "".join(random.sample(s,passlen ))
print(p)
while any(char.isdigit() for char in p) == False:
	p = "".join(random.sample(s,passlen ))
	print(p)
"""

