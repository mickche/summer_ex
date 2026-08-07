# Exercise 9: Rename a Key of Dictionary

def func(my_dict):
     my_dict['first_name'] = my_dict.pop('fname')
     return my_dict

print(func({"fname": "John", "age": 30, "dept": "Engineering"}))
