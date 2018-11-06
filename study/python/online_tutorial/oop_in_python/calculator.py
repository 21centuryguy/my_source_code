def calculator(num1, num2):
	if (type(num1) == type(1) or type(num1) == type(1.0)) and (type(num2) == type(1) or type(num2) == type(1.0)):
		print("1 : addition, 2 : subtraction, 3 : multiplication, 4 : division")
		print("Pleae type a number : ")
		choice_value = input()
		if choice_value == 1:
			print("Your selection is " + str(choice_value))
			return num1 + num2

		elif choice_value == 2:
			print("Your selection is " + str(choice_value))
			return num1 - num2

		elif choice_value == 3:
			print("Your selection is " + str(choice_value))
			return num1 * num2

		elif choice_value == 4:
			print("Your selection is " + str(choice_value))
			return num1 / num2

		else:
			print("Your selection is wrong. Addition is default.")
			return num1 + num2

	else:
		raise ValueError("There's something wrong with your number!")

print(calculator(2, 3.0))
