# Exercise 7: Access ‘history’ Key From a Nested Dictionary

def func(student):
    return student['grades']['history']

print(func({"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}))