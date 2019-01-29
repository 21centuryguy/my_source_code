from gmplot import gmplot
from geoip import geolite2

# get valid ip address
f = open("/Users/jack/Desktop/ip_list.txt", mode="r")
ip_list = f.readlines()
print("Total Ip address count : " + str(len(ip_list)))
valid_latlng_list = []
i = 0
for ip in ip_list:
    ip = ip.strip("\n")
    try:
        match = geolite2.lookup(ip)
        latlng = match.location
        if latlng is not None:
            valid_latlng_list.append(latlng)
        else:
            i = i + 1
    except Exception :
        i = i + 1
print("Invalid ip address count : " + str(i))

# print(valid_latlng_list)
print("Valid ip address count : " + str(len(valid_latlng_list)))

# Place map
gmap = gmplot.GoogleMapPlotter(37.566535, 126.977969, 3)

# Polygon
golden_gate_park_lats, golden_gate_park_lons = zip(*valid_latlng_list)
gmap.scatter(golden_gate_park_lats, golden_gate_park_lons, 'cornflowerblue', marker=10)

# Draw
gmap.draw("/Users/jack/Desktop/ip_latlng_gmap5.html")
