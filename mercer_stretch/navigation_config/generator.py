"""
Generates tour route config file from map coordinates and data
"""


import json

################

# map origin - get this from map.yaml
origin = {"x": -11.1, "y": -11.8, "z": 0}

# resolution - from map.yaml
resolution = 0.05

# start position - coordinate from PGM
# this is called origin in the route files
start = {"x": 186, "y": 374, "z": 0}

# tour stops - coordinates from PGM, program however many you want
# ids are used for audio files. (For id "storefront", the server will look for "storefront.wav")
stops = {
    "Storefront": {"x": 203, "y": 323, "z": 0, "w": 1.0, "id": "storefront"},
    "Tables": {"x": 174, "y": 250, "z": 0, "w": 1.0, "id": "tables"},
    "Workstations": {"x": 227, "y": 113, "z": 0, "w": 1.0, "id": "workstations"},
    "Logo": {"x": 173, "y": 32, "z": 0, "w": 1.0, "id": "logoandhammer"},
    "PCBPrinter": {"x": 284, "y": 171, "z": 0, "w": 1.0, "id": "pcbprinter"},
    "End": {"x": 203, "y": 323, "z": 0, "w": 1.0, "id": "end"}
}
###############


if __name__ == "__main__":
    output = open("generated_route.json", "w")
    for id in stops:
        stops[id]["delay"] = False
        stops[id]["x"] = round(origin["x"] + (stops[id]["x"] * resolution), 2)
        stops[id]["y"] = round(origin["y"] + (stops[id]["y"] * resolution), 2)

        for key in stops[id]:
            if type(stops[id][key]) == int:
                stops[id][key] = float(stops[id][key])

    start["x"] = round(origin["x"] + (start["x"] * resolution), 2)
    start["y"] = round(origin["y"] + (start["y"] * resolution), 2)
    start["w"] = 1.0
    start["delay"] = False
    start["id"] = "origin"
    for key in start:
        if type(start[key]) == int:
            start[key] = float(start[key])

    json.dump({"origin": start, "Poses": stops}, output, indent=2)