# Exercise 10: Delete a List of Keys

def del_list_of_keys(my_dict, list_of_keys):
    # for key in list_of_keys:
    #     if key in my_dict:
    #         del my_dict[key]

    # return my_dict
    return {k:v for k,v in my_dict.items() if k not in list_of_keys}

print(del_list_of_keys({"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"},["stock", "warehouse"]))

#2

# product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
# keys_to_remove = ["stock", "warehouse"]

# for key in keys_to_remove:
#     product.pop(key, None)

# print(product)