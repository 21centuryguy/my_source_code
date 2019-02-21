"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
Chapter 4 Classes & OOP 
4.3 Defining Your Own Exception Classes 
"""

class BaseValidationError(ValueError):
	pass

class NameTooShortError(BaseValidationError):
	pass

class NameTooLongError(BaseValidationError):
	pass

class NameTooCuteError(BaseValidationError):
	pass

def validate(name):
	if len(name) < 10:
		raise NameTooShortError(name)

	elif len(name) > 30:
		raise NameTooLongError(name)

	else:
		raise NameTooCuteError(name)

	try:
		validate(name)
	except BaseValidationError as err:
		handle_validation_error(err)
