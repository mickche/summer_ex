# Exercise 5: Merge Dictionaries

def func(d1,d2):
    d1.update(d2)
    return d1
print(func({"a": 1, "b": 2},{"b": 3, "c": 4}))

#2
def func2(d1,d2):
    return d1 | d2
print(func2({"a": 1, "b": 2},{"b": 3, "c": 4}))


