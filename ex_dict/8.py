# Exercise 8: Initialize Dictionary with Default Value

from collections import defaultdict

def func(keys,default=0):
    my_d = defaultdict(int)

    for key in keys:
        my_d[key] = default  
    return my_d

print(func(["math", "science", "english", "history"]))


#2

# keys = ["math", "science", "english", "history"]
# default = 0

# scores = dict.fromkeys(keys, default)
# print(scores)