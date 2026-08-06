# Exercise 2: Dictionary Operations

def func(car):
    car_psevdo = []
    for k_v in car.items():
        car_psevdo.append(k_v)
    if_brand = None
    if_year = None

    for k in car.keys():
        if k == 'brand':
            if_brand = True
        if k == 'year':
            if_year = True
    return car_psevdo,if_brand,if_year

print(func({"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}))