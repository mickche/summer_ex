# Exercise 14: Map Two Lists (zip)

def func(keys,values):
    return dict(zip(keys,values))

print(func(["brand", "model", "year", "color"], ["Honda", "Civic", 2023, "silver"]))