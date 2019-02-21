"""
<Python Tricks: The Book, A Buffet of Awesome Python Features>
4.1 Object Comparisons: “is” vs “==”
"""


print("#"*30)
a = [1, 2, 3]; print("a = [1, 2, 3]")
b = a; print("b = a")
print("a : ", a)
print("b : ", b)
print("a == b : ", a == b)
print("a is b : ", a is b)

print("\n\n"+"#"*30)
c=list(a); print("c=list(a)")
print("c : ", c)
print("a == c : ", a == c)
print("a is c : ", a is c)


print("\n\n"+"#"*30)
print("An [is] expression evaluates to True if two variables point to the same(identical) object\n" )

print("An [==] expression evalutagte to True if the objects referred to by the variables are equal(have the same contents)\n\n")
