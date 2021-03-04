import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_9_1.json", "w")

fires_data = json.load(infile)

json.dump(fires_data, outfile, indent=4)
# Dump


brightness_list = []

for fire in fires_data:
    bright_instance = fire["brightness"]
    brightness_list.append(bright_instance)


fires_over_450 = [i for i in brightness_list if i > 450]

print(fires_over_450[:10])
# Print out everything from first element to the tenth element
# (0-9)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "brightness": brightness_list,
        "marker": {
            "size": [5 * bright_instance for bright_instance in brightness_list],
            "color": brightness_list,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Global Fires with Brightness over 450")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_fire_brightness.html")
