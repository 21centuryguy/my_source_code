"""
https://www.reddit.com/r/learnpython/comments/3ifgla/making_an_100x100_grid_using_turtle_for_python_3/
"""

import turtle

smart = turtle.Turtle()

width = 20
height = 20
cell_size = 10

for y in range(height):
    for x in range(width):
        smart.up() # Lift the pen
        smart.setposition(x * cell_size, y * cell_size)
        smart.down()

        for i in range(4):
            smart.forward(10)
            smart.right(90)
 