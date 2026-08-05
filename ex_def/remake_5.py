def multi(num,m):
    def inner(m):
        return num * m
    return inner(m)

print(multi(2,2))