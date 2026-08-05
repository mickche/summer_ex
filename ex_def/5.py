def func(a,b):
    def inner(a,b):
        return a+b
    return inner(a, b) + 5
print(func(5,10))