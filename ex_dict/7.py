# Exercise 7: Access ‘history’ Key From a Nested Dictionary

def get_grage_of_history(student):
    return student['grades']['history']

print(get_grage_of_history({"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}))