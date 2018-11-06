"""
https://stackoverflow.com/questions/14730475/python-turtle-window-with-scrollbars
"""

import turtle

win_width, win_height, bg_color = 2000, 2000, 'black'

turtle.setup()
turtle.screensize(win_width, win_height, bg_color)

t = turtle.Turtle()
#t.hideturtle()
#t.speed(0)
t.color('white')

for _ in range(4):
    t.forward(500)
    t.right(90)

turtle.done()