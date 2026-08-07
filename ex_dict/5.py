# Exercise 5: Merge Dictionaries

def merge(d1,d2):
    d1.update(d2)
    return d1
print(merge({"a": 1, "b": 2},{"b": 3, "c": 4}))

#2
def merge2(d1,d2):
    return d1 | d2
print(merge2({"a": 1, "b": 2},{"b": 3, "c": 4}))


