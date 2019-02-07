from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.566535, 126.977969, 3)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*[
    (1.293100, 103.855800),
    (30.05, 31.3666),
    (44.8033, 22.9719),
    (38.0, -97.0),
    (37.773646, -122.440979),
    (37.772742, -122.440797),
    (37.771096, -122.453889),
    (37.768669, -122.453518),
    (37.766227, -122.460213),
    (37.764028, -122.510347),
    (37.771269, -122.511015)
    ])
gmap.scatter(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', marker=10)

# Draw
gmap.draw("/Users/jack/Desktop/ip_latlng_gmap3.html")
