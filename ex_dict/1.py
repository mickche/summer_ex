# Exercise 1: Basic Dictionary Operations

def func(student):
    student.update({'age':21})
    return student,f"Name: {student['name']}"

print(*func({"name": "Alice", "age": 20, "grade": "B"}))

