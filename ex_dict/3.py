# Exercise 3: Dictionary from Two Lists

def two_in_one(l1,l2) -> dict:
    d = {}
    for k in l1:
        for v in l2:
            d[k] = v
    return d
print(two_in_one(["name", "age", "city"],["Bob", 25, "London"]))


#2

def two_in_one_2(l1,l2):
    return dict(zip(l1,l2))

print(two_in_one_2(["name", "age", "city"],["Bob", 25, "London"]))