######################################
# A simple ascending sort is very easy -- just call the sorted() function. It returns a new sorted list:

>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]

######################################
# You can also use the list.sort() method of a list. It modifies the list in-place (and returns None to avoid confusion). Usually it's less convenient than sorted() - but if you don't need the original list, it's slightly more efficient.

>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]

######################################
# Another difference is that the list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.

>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]

######################################

