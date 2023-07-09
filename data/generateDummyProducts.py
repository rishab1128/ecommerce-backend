import random
import json

# List of electronic items
electronic_items = ["TV", "Mobile", "Laptop", "Headphones", "Tablet", "Smartwatch", "Camera", "Speakers"]

# Generate 20 random electronic products
products = []
for _ in range(20):
    product = {
        "Name": random.choice(electronic_items),
        "Price": random.randint(100, 10000),
        "Qty": random.randint(1, 100)
    }
    products.append(product)

# Save products to JSON file
with open("products.json", "w") as json_file:
    json.dump(products, json_file, indent=4)

print("Products have been saved to products.json file.")
