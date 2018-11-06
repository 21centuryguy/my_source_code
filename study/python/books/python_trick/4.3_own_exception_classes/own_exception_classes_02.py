"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
Chapter 4 Classes & OOP 
4.3 Defining Your Own Exception Classes 
"""

class NameTooShortError(ValueError):
	pass

def validate(name):
	if len(name) < 10:
		raise NameTooShortError(name)

