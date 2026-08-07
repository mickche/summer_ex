# Exercise 1: Basic Dictionary Operations

def make_student(student):
    student.update({'age':21})
    return student,f"Name: {student['name']}"

print(*make_student({"name": "Alice", "age": 20, "grade": "B"}))

