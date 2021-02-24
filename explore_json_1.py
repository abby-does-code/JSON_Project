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

mags = []
