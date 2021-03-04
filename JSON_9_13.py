import json


infile = open("US_fires_9_14.json", "r")
outfile = open("readable_9_14.json", "w")

fires_data = json.load(infile)

json.dump(fires_data, outfile, indent=4)
# Dump


brightness_list, lons, lats = [], [], []

for x in fires_data:
    bright_instance = x["brightness"]
    lon = x["longitude"]
    # This calls the dictionary, the list (geometry) and the index number of #longitude in the list (0)
    lat = x["latitude"]

    brightness_list.append(bright_instance)
    lons.append(lon)
    lats.append(lat)


fires_over_450 = [i for i in brightness_list if i > 450]
print(fires_over_450[:10])
print(lats[:10])
# Print out everything from first element to the tenth element


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline as offline


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": brightness_list,
        "marker": {
            "size": [5 * bright_instance for bright_instance in brightness_list],
            "color": brightness_list,
            "colorscale": "Viridis",
            "reversescale": True,
            # "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fires with Brightness over 450")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="fire_brightness_2.html")
