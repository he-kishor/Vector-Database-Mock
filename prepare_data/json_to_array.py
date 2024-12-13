import numpy as np
import json
# Extracting data into separate arrays
fileName = "product.json"
with open(fileName, 'r') as json_file:
    data = json.load(json_file)


names = [item["name"] for item in data]
descriptions = [item["description"] for item in data]
embeddings = [item["embedding"] for item in data]

print(names,"/n")
print(descriptions,"/n")
print(embeddings,"/n")

