a = 10                          # variable

def f(b):                       # function  
    return b ** 2

class C:

    c = 20                      # class attribute

    def __init__(self, d):      # "dunder" method
        self.d = d              # instance attribute

    def show(self):             # method
        print(self.c, self.d) 

e = C(30)
e.g = 40 