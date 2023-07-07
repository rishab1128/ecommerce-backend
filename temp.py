import random
from faker import Faker

fake = Faker()

def generate_city_data(num_cities):
    city_data = []
    
    for _ in range(num_cities):
        city = fake.city()
        country = fake.country()
        city_data.append((city, country))
    
    return city_data

if __name__ == '__main__':
    num_cities = 100
    cities = generate_city_data(num_cities)

    (city,country) = cities[0]
    print(cities[0])
    print(city)
    print(country)
    
    # for city, country in cities:
    #     print(f"City: {city}, Country: {country}")
