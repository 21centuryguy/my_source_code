"""
https://medium.freecodecamp.org/an-a-z-of-useful-python-tricks-b467524ee747
"""

x = [True, True, False]

if any(x):
	print("1. At least one True")

if all(x):
	print("2. Not one False")

if any(x) and not all(x):
	print("3. At least one True and one False")

