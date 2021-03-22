import json
import pandas

with open("data.json", 'r+') as f:
    d = json.load(f)

necklace_sets = []
description = []
images = []
prices = []
for i in d:
    key = str(i.keys()).split('\'')[1]
    values = list(i.values())[0]
    for value in values:
        data = list(value.values())
        image, desc, price = data[0], data[1], data[2]
        necklace_sets.append(key)
        description.append(desc)
        images.append(image)
        prices.append(price)

df = pandas.DataFrame(data=[necklace_sets, description, images, prices]).transpose()
df.columns = ['Necklace Set', 'Description', 'Image Url', 'Price']

df.to_csv("data.csv")
