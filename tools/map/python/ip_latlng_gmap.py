import gmplot
from geoip import geolite2

def get_latlng_from_ip(ip_address):
	match = geolite2.lookup(ip_address)
	latlng = match.location
	print(list(latlng)[0])
	print(list(latlng)[1])
	return latlng

def draw_map(latlng, zoom_input):
	input("Zoom : ")
	gmap = gmplot.GoogleMapPlotter(getlatlng(latlng, zoom_input)
	# Marker
	hidden_gem_lat, hidden_gem_lon = list(latlng)[0], list(latlng)[1]
	gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title="test")
 	gmap.draw("/Users/jack/Desktop/ip_latlng_gmap.html") 

ip_address = input("IP address : ")
get_latlng_from_ip(ip_address)
# draw_map(latlng, zoom_input)
