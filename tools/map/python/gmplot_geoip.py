'''import gmplot package'''
import gmplot

''' 
GoogleMapPlotter return Map object 
Pass the center latitude and 
#center longitude
'''
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 11) # San Francisco
# gmap = gmplot.GoogleMapPlotter.from_geocode("San Francisco")

# Pass the absolute path
gmap.draw("/Users/jack/Desktop/maptest.html") 
