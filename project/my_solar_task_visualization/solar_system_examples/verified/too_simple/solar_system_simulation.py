# http://meltedred.com/solar-system-simulation-in-python.html
# solar_system_simulation.py

import ephem
import time
import datetime
import visual
import numpy as np

AU = 149597871/100.0

def get_day(d):
    return "{}/{}/{}".format(d.year, d.month, d.day)

#visual.scene.autoscale = False
day = datetime.datetime(2014, 1, 1)

one_day = datetime.timedelta(days=1)

sun = visual.sphere(radius=695800, color=visual.color.yellow)
planets = [ephem.Mercury(), ephem.Venus(), ephem.Sun(), ephem.Mars(), 
           ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(), ephem.Neptune(),
           ephem.Pluto()]

class Planet2(object):
    def __init__(self, planet):
        self.planet = planet

planets = [Planet2(planet) for planet in planets]

planets[0].sphere = visual.sphere(radius=2440, color=(.8,.8,.8),
                                  make_trail=True)

planets[1].sphere = visual.sphere(radius=3760, color=visual.color.yellow,
                                  make_trail=True)

planets[2].sphere = visual.sphere(radius=3959, color=visual.color.blue,
                                  make_trail=True)

planets[3].sphere = visual.sphere(radius=3390, color=visual.color.red,
                                  make_trail=True)

planets[4].sphere = visual.sphere(radius=43441, color=visual.color.red,
                                  make_trail=True)
assert(planets[4].sphere != None)

planets[5].sphere = visual.sphere(radius=36184, color=visual.color.orange,
                                  make_trail=True)

planets[6].sphere = visual.sphere(radius=15759, color=visual.color.yellow,
                                  make_trail=True)

planets[7].sphere = visual.sphere(radius=15299, color=visual.color.blue,
                                  make_trail=True)

planets[8].sphere = visual.sphere(radius=736, color=(.8,.8,.8),
                                  make_trail=True)

DAYS = 248*365 #mars year

for _ in range(DAYS):
    for planet in planets:
        eplanet = planet.planet
        eplanet.compute(get_day(day))

        dist = AU*eplanet.sun_distance

        lat = eplanet.hlat
        lon = eplanet.hlon

        x = dist * np.cos(lat) * np.cos(lon)
        y = dist * np.cos(lat) * np.sin(lon)
        z = dist * np.sin(lat)


        planet.sphere.pos = visual.vector(x, y, z)

    day += one_day