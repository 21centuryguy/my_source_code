from geoip import geolite2
match = geolite2.lookup('17.0.0.1')
print(match.country)
print(match.continent)
print(match.timezone)
print(match.subdivisions)
