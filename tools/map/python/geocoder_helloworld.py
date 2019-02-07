import geocoder

g = geocoder.google('Mountain View')
print(g.latlng)

"""
g = geocoder.mapquest(['Mountain View, CA', 'Boulder, Co'], method='batch')
for result in g:
	print(result.address, result.latlng)
"""