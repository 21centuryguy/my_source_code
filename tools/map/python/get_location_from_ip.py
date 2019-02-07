import googlemaps, gmplot, webbrowser, os, json

gmaps = googlemaps.Client(key='XXX') 
geocode_result = gmaps.geocode('100 Broadway Street, Missoula, MT')

#######
gmap = gmplot.GoogleMapPlotter.from_geocode("Missoula")    # IF THIS LINE IS HERE, IT THROWS THE ERROR
#######

geom = geocode_result[0]['geometry']
loc = geom['location']
lat = loc['lat']
lng = loc['lng']

#######
gmap = gmplot.GoogleMapPlotter.from_geocode("Missoula")    # IF THIS LINE IS HERE, IT WORKS
#######

hidden_gem_lat, hidden_gem_lon = lat,lng
gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

# Draw
gmap.draw("my_map.html")

filename = 'file:///'+os.getcwd()+'/' + 'my_map.html'
webbrowser.open_new_tab(filename)