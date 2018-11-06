"""import math

def hypotenuse(a, b):
	if type(a) == type(1) and type(b) == type(1):
		return math.sqrt(a**2 + b**2)
		 
	else:
		return "You must put number only!"
 
print(hypotenuse(24, 36))
print(hypotenuse("ten", "three"))
print(hypotenuse(10, "three"))"""

import math

def hypotenuse(x, y):
    try:
        return math.sqrt(x**2 + y**2)
    except TypeError:
        return None

print(hypotenuse(12, 34))
print(hypotenuse("12", "34"))
print(hypotenuse(12, "34"))
