"""
https://www.tutorialspoint.com/numpy/numpy_indexing_and_slicing.htm
"""

import numpy as np

print('######## [ a = np.arange(10) ] #############')
a = np.arange(10)

# case 1
print('print(a)')
print(a)
print('\n')

# case 2
s = slice(2,7,2)
print('print(a[s])')
print(a[s])
print('\n')

# case 3
b = a[2:7:2]
print('print(b)')
print(b)
print('\n')

# case 4
print('print(a[5])')
print(a[5])
print('\n')

# case 5
print('print(a[2:5])')
print(a[2:5])
print('\n')


print('######## [ a = np.array([[1,2,3],[3,4,5],[4,5,6]]) ] #############')

a = np.array([[1,2,3],[3,4,5],[4,5,6]])

# case 6
print('print(np.array([[1,2,3],[3,4,5],[4,5,6]]))')
print(np.array([[1,2,3],[3,4,5],[4,5,6]]))
print('\n')

# case 7
print('Now we will slice the array from the index a[1:]')
print('print(a[1:])')
print(a[1:])
print('\n')

# case 8
print('>>>>>>> column <<<<<<<')
print('\n')

print('Our array is:')
print(a)
print('\n')

# this retruns array of items in the first column
print('The items in the first column are:')
print(a[...,0])
print('\n')

# this retruns array of items in the first column
print('The items in the second column are:')
print(a[...,1])
print('\n')

# this retruns array of items in the first column

print('The items in the third column are:')
print(a[...,2])
print('\n')


# case 9
print('>>>>>>> row <<<<<<<')
print('\n')

print('Our array is:')
print(a)
print('\n')

print('>>>>>>> The items in the first row are: <<<<<<<')
print(a[0,...])
print('\n')

# this retruns array of items in the second row
print('>>>>>>> The items in the second row are: <<<<<<<')
print(a[1,...])
print('\n')

# this retruns array of items in the third row
print('>>>>>>> The items in the third row are: <<<<<<<')
print(a[2,...])
print('\n')


# case 10
print('Our array is:')
print(a)
print('\n')

print('>>>>>>> The items column 1 onwards are:  <<<<<<<')
print('\n')

print('The items column 1 onwards are:')
print(a[...,1:])
print('\n')

# case 11
print('Our array is:')
print(a)
print('\n')

print('>>>>>>> The items row 1 onwards are:  <<<<<<<')
print('\n')

print('The items row 1 onwards are:')
print(a[1:,...])
print('\n')





