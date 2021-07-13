import json

with open('cars_manufacturer.json', 'r') as in_file:
    orig = json.load(in_file)

i = 1
data_copy = orig.copy()
for item in data_copy:
    i += 1
    item["id"] = i
    item["raw_image"] = item["image"]["original"]
    item.pop("image")
    item.pop("slug")


with open('cars_manufacturer_V2.json', 'w') as out_file:
    json.dump(data_copy, out_file, indent=4)
