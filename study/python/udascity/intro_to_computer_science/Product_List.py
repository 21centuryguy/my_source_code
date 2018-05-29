# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
	m = 0
	n = 1
	while m < len(list_of_numbers):
		list_of_numbers[m]
		n = n*list_of_numbers[m]
		# print m
		m = m + 1
	return n

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1