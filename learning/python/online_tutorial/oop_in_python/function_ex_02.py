def divide(dividend, divisor):
	quotient = dividend // divisor
	remainder = dividend % divisor
	return quotient, remainder

# you can do this
q, r = divide(35, 4)
print(q, r)

# but you can also do this
result = divide(67, 9)
q1 = result[0]
q2 = result[1]
print("result : " + str(result))
print(q1, q2)


# by the way, you can also do this
a, b = (1, 2)
print(a, b)

# or this
c, d = [5, 6]
print(c, d)
