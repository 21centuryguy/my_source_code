# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(p):
	total = 1
	for i in p:
		total = total*i
	return total

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1