import json

infile = open("eq.data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "r")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)
# Dump
