# Exercise 3: Dictionary from Two Lists

def two_in_one(list1,list2) -> dict:
    my_dict = {}
    for key in list1:
        for value in list2:
            my_dict[key] = value
    return my_dict
print(two_in_one(["name", "age", "city"],["Bob", 25, "London"]))


#2

def two_in_one_2(l1,l2):
    return dict(zip(l1,l2))

print(two_in_one_2(["name", "age", "city"],["Bob", 25, "London"]))