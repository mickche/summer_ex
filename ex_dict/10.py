# Exercise 10: Delete a List of Keys


def func(d,l_of_k):
    for k in l_of_k:
        if k in d:
            del d[k]

    return d

print(func({"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"},["stock", "warehouse"]))

#2

# product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
# keys_to_remove = ["stock", "warehouse"]

# for key in keys_to_remove:
#     product.pop(key, None)

# print(product)