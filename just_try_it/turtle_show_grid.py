import turtle
bob = turtle.Turtle()

def square(side):
    for i in range(4):
        bob.forward(side)
        bob.left(90)

def row(n, side):
    for i in range(n):
        square(side)
        bob.forward(side)
    bob.penup()
    bob.left(180)
    bob.forward(n * side)
    bob.left(180)
    bob.pendown()

def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
        bob.penup()
        bob.left(90)
        bob.forward(side)
        bob.right(90)
        bob.pendown()
    bob.penup()
    bob.right(90)
    bob.forward(m * side)
    bob.left(90)
    bob.pendown()

row_of_rows(4,5, 20)