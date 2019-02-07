import gmplot
# from gmplot import gmplot

location_input = input("Type your target location >>> ")

gmap = gmplot.GoogleMapPlotter.from_geocode(location_input, 'XXX')

gmap.draw("/Users/jack/Desktop/maptest4.html") 
