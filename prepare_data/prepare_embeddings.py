import numpy as np
import json

fileName = "product.json"
with open(fileName, 'r') as json_file:
    product_data = json.load(json_file)

num_products = len(product_data)
embeddings = np.random.rand(num_products,5).round(4)

for i, product in enumerate(product_data):
    product['embedding']=embeddings[i].tolist()
    
with open(fileName, 'w') as json_file:
        json.dump(product_data, json_file, indent=2)
