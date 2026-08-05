def func(a,b):
    def inner():
        return a+b
    return inner() + 5
print(func(5,10))