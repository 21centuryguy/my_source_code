import geocoder
import gmplot

location_input = input("Type your target location >>> ")
zoom_input = input("Type map zoom value >>> ")

def getlatlng(location_input):
	g = geocoder.google(location_input)
	# print(g.latlng)
	return(g.latlng)

# GoogleMapPlotter return Map object
gmap = gmplot.GoogleMapPlotter(getlatlng(location_input)[0], getlatlng(location_input)[1], zoom_input)

# Marker
hidden_gem_lat, hidden_gem_lon = getlatlng(location_input)[0], getlatlng(location_input)[1]
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title="test")

gmap.draw("/Users/jack/Desktop/maptest5.html") 
