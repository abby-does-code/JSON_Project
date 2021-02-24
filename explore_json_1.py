import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)
# Dump

# print(eq_data["features"][0])
# With this line of code, we get a dictionary back!

# Version 2:
# print(eq_data["features"][0]["properties"]["mag"])
# This one takes us exactly to what we wanted--the magnited. But this is just the first one!

mags, lons, lats = [], [], []
# Creates three lists; magnitudes, longitudes, and latitudes

list_of_eqs = eq_data["features"]

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    # This calls the dictionary, the list (geometry) and the index number of #longitude in the list (0)
    lat = eq["geometry"]["coordinates"][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
# Print out everything from first element to the tenth element
# (0-9)
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
