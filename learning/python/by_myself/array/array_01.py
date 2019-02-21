
print("="*100)

print "Arrays are fundamental part of most programming languages."
print "It is the collection of elements of a single data type, eg. array of int, array of string."
print "However, in Python, there is no native array data structure. So, we use Python lists instead of an array."
print "Note: If you want to create real arrays in Python, you need to use NumPy's array data structure."
print "For mathematical problems, NumPy Array is more efficient."
print "Unlike arrays, a single list can store elements of any data type and does everything an array does." 
print "We can store an integer, a float and a string inside the same list. So, it is more flexible to work with."
print "\n"
print "https://www.programiz.com/python-programming/array"


print("="*100)
print("\n")

# Create an Array / Access elements of an Array / Negative Indexing ##################################
arr = [10, 20, 30, 40, 50]
print (arr[0])
print (arr[1])
print (arr[2])
print(arr[-1])
print(arr[-2])

print("="*100)
print("\n")

# Find length of an Array ##################################
brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
num_brands = len(brands)
print(num_brands)

print("="*100)
print("\n")

# Add an element to an Array ##################################
add = ['a', 'b', 'c']
add.append('d')
print(add)

print("="*100)
print("\n")

# Remove elements from an Array ##################################
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4] ### yellow
print(colors)
colors.remove("blue") ### blue
print(colors)
colors.pop(3) ### orange
print(colors)

print("="*100)
print("\n")

# Modify elements of an Array ##################################
fruits = ["Apple", "Banna", "Manog", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)

print("="*100)
print("\n")

# Python operators to modify elements in  an Array ##################################
concat = [1, 2, 3]
concat += [4, 5, 6] # concat = concat + [4, 5, 6]
print(concat)

print("="*100)
print("\n")

# Python operators to modify elements in  an Array ##################################
repeat = ["a"]
repeat = repeat*5
print(repeat)

print("="*100)
print("\n")

# Slicing an Array ##################################

fruits = ["Apple", "Banna", "Manog", "Grapes", "Orange"]
print(fruits[1:4]) ### 1, 2, 3
print(fruits[:3]) ### 0, 1, 2
print(fruits[-4:]) ### -4, -3, -2, -1  = 1, 2, 3, 4
print(fruits[-3:-1]) ### -3, -2 = 2, 3

print("="*100)
print("\n")

# Multidimensional arrays ##################################

multd = [[1,2 ], [3,4], [5,6], [7,8]]
print[multd[0]]
print[multd[3]]
print[multd[2][1]]
print[multd[3][0]]


print("="*100)
print("\n")

###################################







