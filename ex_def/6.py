def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0

print(addition(10))