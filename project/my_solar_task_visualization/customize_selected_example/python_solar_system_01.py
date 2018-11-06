# -*- coding: utf-8 -*-
""" 
https://www.daniweb.com/programming/software-development/threads/475514/python-turtle
python_solar_system
"""

from turtle import Shape, Turtle, mainloop, Vec2D as Vec
# from time import sleep
# Turtle.bgcolor("black")
G = 8 # 8  ### 숫자가 작아도 커도 궤도가 원이 아니라 직선이 되거나 이상하게 돌아


class Gravity(object):
    print("Gravity(object)")
    """Gravity"""
    def __init__(self):
        print("xxx")
        self.planets = []
        self.time = 0
        self.distance = 0.1
    def init(self):
        print("init(self)")
        for planet in self.planets:
            planet.init()
    def start(self):
        print("start(self)")
        for i in range(5000000000): ### 500
            self.time += self.distance
            for planet in self.planets:
                planet.step()


class Planet(Turtle):
    """Planet"""
    print("Planet(Turtle)")
    def __init__(self, mass, x_pos, velocity, gravity, shape):
        print("__init__(self, mass, x_pos, velocity, gravity, shape)")
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.mass = mass
        self.setpos(x_pos)
        self.velocity = velocity
        gravity.planets.append(self)
        self.gravity = gravity
        self.resizemode("user")
        # self.pendown()  ### with trace line
        self.pu() ### no trace line
        # self.write("This is my cuty task^^")
    def init(self):
        print("init(self)")
        distance = self.gravity.distance
        self.a = self.acc()
        self.velocity = self.velocity + 0.5 * distance * self.a
    def acc(self):
        print("acc(self)")
        a = Vec(0, 0)
        for planet in self.gravity.planets:
            if planet != self:
                velocity = planet.pos()-self.pos()
                a += (G*planet.mass/abs(velocity)**3)*velocity
        return a
    def step(self):
        print("step(self)")
        distance = self.gravity.distance
        self.setpos(self.pos() + distance * self.velocity)
        if self.gravity.planets.index(self) != 0:
            self.setheading(self.towards(self.gravity.planets[0]))
        self.a = self.acc()
        self.velocity = self.velocity + distance * self.a


def main():
    """create compound yellow/blue turtleshape for planets"""
    print ("main()")
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0, 0)
    s.ht()  #hide turtle
    s.pu()  #pen up
    s.fd(6)  # forward
    s.lt(90)  #lt
    s.begin_poly()  #begining of the polygon, the current position is the first vecto of the polygon
    s.circle(2)  ###  circle size
    s.end_poly()  #end the polygon
    #creates m1, creats a semi circle  
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(5) 
    s.end_poly()
    #creates m2, uses the specs from the last recorded poly ^
    #m2 = s.get_poly()
    planetshape = Shape("compound")
    planetshape.addcomponent(m1, "green")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(2, 0)  ### speed

    """setup gravitational system"""
    gs = Gravity()
    sun = Planet(1000000, Vec(0, 0), Vec(0, 0), gs, "circle")
    sun.color("yellow")
    sun.shapesize(5)
    sun.pu()  ### Pull the pen up – no drawing when moving.
    earth = Planet(12500, Vec(215, 0), Vec(0, 195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(2)
    earth.write("This is my cuty task 111")
    moon = Planet(1, Vec(225, 0), Vec(0, 295), gs, 'planet')
    moon.pencolor('blue')
    moon.shapesize(1)
    moon.write("This is my cuty task 222")
    mars = Planet(4000, Vec(0, 327), Vec(150, 0), gs, "planet")
    mars.pencolor('red')
    mars.shapesize(5)
    mars.write("This is my cuty task 444")
    jupiter = Planet(750, Vec(-430, 0), Vec(0, 100), gs, "planet")
    jupiter.pencolor('purple')
    jupiter.shapesize(3)
    jupiter.write("This is my cuty task 555")
    # p5 = Planet (mass, x_pos, velocity, gravity, shape)
    # p6 = (name, radius), mass, colour, distance, x velocity, y velocity
    gs.init()
    gs.start()
    # s.onclick(pause)
    return "Done!"
if __name__ == '__main__':
    print("name==main")
    msg = main()
    print(msg)
    mainloop()
