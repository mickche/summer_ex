# Exercise 6: Access Nested Dictionary

def func(person:dict) -> str:
    return person['address']['city']

print(f'City: {func({"name": "Carol", "address": {"city": "Paris", "zip": "75001"}})}')