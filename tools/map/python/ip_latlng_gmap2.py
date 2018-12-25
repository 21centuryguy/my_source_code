import gmplot
from geoip import geolite2

ip_address = input("IP address : ")
match = geolite2.lookup(ip_address)
latlng = match.location
print(latlng)

# zoom_input = input("Zoom : ")
zoom_input = 3.5

gmap = gmplot.GoogleMapPlotter(list(latlng)[0], list(latlng)[1], zoom_input)
hidden_gem_lat, hidden_gem_lon = list(latlng)[0], list(latlng)[1]
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue', title="test")

gmap.draw("/Users/jack/Desktop/ip_latlng_gmap2.html")
