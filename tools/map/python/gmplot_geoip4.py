import gmplot
# from gmplot import gmplot

location_input = input("Type your target location >>> ")

gmap = gmplot.GoogleMapPlotter.from_geocode(location_input, 'AIzaSyCIjvLJuxDaUzVa-nG7UH9P7nZFnO-PB-E')

gmap.draw("/Users/jack/Desktop/maptest4.html") 
