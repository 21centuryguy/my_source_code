# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
[ python2 ]
# https://svn.python.org/projects/python/trunk/Demo/turtle/tdemo_planet_and_moon.py

turtle-example-suite:

tdemo_planets_and_moon.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light moon!
Planet has a circular orbit, moon a stable
orbit around the planet.

You can hold the movement temporarily by pressing
the left mouse button with mouse over the
scrollbar of the canvas.

"""
from turtle import Screen, Shape, Turtle, mainloop, Vec2D as Vec
from time import sleep

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000000000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        # self.pendown()
        self.pu()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a

## create compound yellow/blue turtleshape for planets

def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    # s.getscreen().getcanvas()
    s.ht()
    s.pu()
    s.fd(6) # s.fd(6) ### 숫자를 키우면 달이 지구 속도를 못 따라와
    s.lt(90) # lt(90)
    s.begin_poly()
    s.circle(6, 180) # s.circle(6, 180) ### 숫자를 키우면 지구와 달의 사이즈가 커져
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(100,0) ### speed

    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
    # sun = Star(1, Vec(0,0), Vec(0,-2.5), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()
    earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
    # earth = Star(1, Vec(210,0), Vec(0,195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
    # moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print (msg)
    mainloop()