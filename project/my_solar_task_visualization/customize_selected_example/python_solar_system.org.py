""" 
https://www.daniweb.com/programming/software-development/threads/475514/python-turtle

python_solar_system
"""
from turtle import Shape, Turtle, mainloop, Vec2D as Vec 
from time import sleep
#Turtle.bgcolor("black")
G = 8
class Gravity(object):
    def __init__(self):
        self.planets = []
        self.time = 0
        self.distance = 0.1
    def init(self):
        for planet in self.planets:
            planet.init()
    def start(self):
        for i in range(500):
            self.time += self.distance
            for planet in self.planets:
                planet.step()
class Planet(Turtle):
    def __init__(self, mass, x_pos, velocity, gravity, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.mass = mass
        self.setpos(x_pos)
        self.velocity = velocity
        gravity.planets.append(self)
        self.gravity = gravity
        self.resizemode("user")
        self.pendown()
    def init(self):
        distance = self.gravity.distance
        self.a = self.acc()
        self.velocity = self.velocity + 0.5 * distance * self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravity.planets:
            if planet != self:
                velocity = planet.pos()-self.pos()
                a += (G*planet.mass/abs(velocity)**3)*velocity
        return a
    def step(self):
        distance = self.gravity.distance
        self.setpos(self.pos() + distance * self.velocity)
        if self.gravity.planets.index(self) != 0:
            self.setheading(self.towards(self.gravity.planets[0]))
        self.a = self.acc()
        self.velocity = self.velocity + distance * self.a
## create compound yellow/blue turtleshape for planets
def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht() #hide turtle
    s.pu() #pen up
    s.fd(6) # forward
    s.lt(90) #lt
    s.begin_poly() #begining of the polygon, the current position is the first vecto of the polygon
    s.circle(5) 
    s.end_poly() #end the polygon
    #creates m1, creats a semi circle  
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(5)
    s.end_poly()
    #creates m2, uses the specs from the last recorded poly ^
    #m2 = s.get_poly()
    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"green")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)
    ## setup gravitational system
    gs = Gravity()
    sun = Planet(1000000, Vec(0,0), Vec(0,0), gs, "circle")
    sun.color("yellow")
    sun.shapesize(5)
    sun.pu()
    earth = Planet(12500, Vec(215,0), Vec(0,195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(2)
    moon = Planet(1, Vec(225,0), Vec(0,295),gs, 'planet')
    moon.pencolor('blue')
    moon.shapesize(1)
    mars = Planet(4000, Vec(0,327), Vec(150,0), gs, "planet")
    mars.pencolor('red')
    mars.shapesize(2)
    jupiter = Planet(750, Vec(-430,0), Vec(0,100), gs, "planet")
    jupiter.pencolor('purple')
    jupiter.shapesize(3)
 #   p5 = Planet (mass, x_pos, velocity, gravity, shape)
 #   p6 = (name, radius), mass, colour, distance, x velocity, y velocity
    gs.init()
    gs.start()
#   s.onclick(pause)
    return "Done!"
if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()