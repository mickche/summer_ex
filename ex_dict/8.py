# Exercise 8: Initialize Dictionary with Default Value

def defalt_values(keys,default=0):
    return {key:default for key in keys}
print(defalt_values(["math", "science", "english", "history"]))


#2

# keys = ["math", "science", "english", "history"]
# default = 0

# scores = dict.fromkeys(keys, default)
# print(scores)