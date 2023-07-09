import json
from datetime import datetime
import random
import string
from faker import Faker

fake = Faker()


def generate_city_data(num_cities):
    city_data = []

    for _ in range(num_cities):
        city = fake.city()
        country = fake.country()
        city_data.append((city, country))

    return city_data


def generate_dummy_data():
    dummy_data = []
    cities = generate_city_data(20)
    for _ in range(20):
        random_timestamp = datetime.now().isoformat()

        random_total_amount = round(random.uniform(10.0, 100.0), 2)

        random_city, random_country = cities[random.randint(0, 19)]

        random_zip_code = ''.join(random.choices(string.digits, k=5))

        num_items = random.randint(2, 5)
        random_items = []
        for _ in range(num_items):
            random_items.append({
                "product_id": random.randint(1, 7),
                "bought_quantity": random.randint(1, 10)
            })

        random_user_address = {
            "city": random_city,
            "country": random_country,
            "zip_code": random_zip_code
        }

        dummy_entry = {
            "timestamp": random_timestamp,
            "items": random_items,
            "total_amount": random_total_amount,
            "user_address": random_user_address
        }

        
        dummy_data.append(dummy_entry)

    return dummy_data


# Generate dummy data
dummy_data = generate_dummy_data()
print(dummy_data[0])

# Save to JSON file
with open('orders.json', 'w') as f:
    json.dump(dummy_data, f, indent=4)

print("Dummy data file 'orders.json' has been generated.")
