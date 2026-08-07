# Exercise 6: Access Nested Dictionary

def about_person(person:dict) -> str:
    return person['address']['city']

print(f'City: {about_person({"name": "Carol", "address": {"city": "Paris", "zip": "75001"}})}')