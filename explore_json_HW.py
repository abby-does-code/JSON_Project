import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_9_1.json", "w")

fires_data = json.load(infile)

json.dump(fires_data, outfile, indent=4)
# Dump

# print(fires_data["brightness"][:10])


fires_over_450 = fires_data["brightness"]

for element in infile:
    if infile.brightness > 450:
        fires_over_450.append(brightness)

print(fires_over_450[:10])
# Print out everything from first element to the tenth element
# (0-9)

"""
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
"""